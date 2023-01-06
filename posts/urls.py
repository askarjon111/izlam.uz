from django.urls import path
from posts.views import HomeView, PostsView, load_more, SinglePost


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('posts/', PostsView.as_view(), name="post_list"),
    path('posts/load-more', load_more, name="load"),
    path('posts/<int:pk>/', SinglePost.as_view(), name="single_post"),
]
