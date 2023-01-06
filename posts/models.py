from django.db import models
from ckeditor.fields import RichTextField 


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500, verbose_name="Sarlavha")
    body = RichTextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to="covers", null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    published_at = models.DateField(null=True, auto_now_add=True)

    is_published = models.BooleanField(default=True)
    is_top = models.BooleanField(default=False)

    def __str__(self):
        return self.title
