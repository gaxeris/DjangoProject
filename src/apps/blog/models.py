
from django.db import models
from django.urls import reverse

from apps.blog.managers import PostManager


# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):

    title = models.CharField(max_length=150)
    text = models.TextField()
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    slug = models.SlugField(unique=True)
    
    # base manager eксtension
    objects = PostManager()
    
    def __str__(self):
        return self.title 
    
    def get_unique_slug(self):
        slug = reverse(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}{num}"
            num += 1
        return unique_slug
    
    
    
