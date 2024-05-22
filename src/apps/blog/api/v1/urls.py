from rest_framework import routers
from django.urls import path

from apps.blog.api.v1.views import AuthorsViewSet, CategoryViewSet, PostViewSet



router_blog = routers.DefaultRouter()


router_blog.register(r'posts', PostViewSet)
router_blog.register(r'categories', CategoryViewSet)
router_blog.register(r'authors', AuthorsViewSet)

