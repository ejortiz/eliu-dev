from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

def thumbnails_path():
    return os.path.join(settings.IMAGES_PATH, 'blog')

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    content_preview = models.CharField(max_length=200, default="")
    thumbnail_path = models.FilePathField(path=thumbnails_path, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title