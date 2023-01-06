from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from posts.models import Post


class HomeView(ListView):
    queryset = Post.objects.order_by('-is_top')[:9]
    template_name = 'pages/home.html'


class PostsView(ListView):
    queryset = Post.objects.order_by('-id')[:9]


def load_more(request):
    loaded_item = request.GET.get('loaded_item')
    loaded_item_int = int(loaded_item)
    limit = 3
    object_list = list(Post.objects.values()[loaded_item_int:loaded_item_int+limit])
    data = {'object_list': object_list}
    return JsonResponse(data=data)


class SinglePost(DetailView):
    template_name = 'posts/single_post.html'
    queryset = Post.objects.all()
