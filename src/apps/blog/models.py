from ast import mod
from django.db import models

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    
    slug = models.SlugField(unique=True)
    
    
    


class Post(models.Model):
    
    name = models.CharField(max_length=150)
    
    created = models.DateTimeField(auto_now_add=True)
    
    slug = models.SlugField(unique=True)    