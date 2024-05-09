
from rest_framework import viewsets

from apps.blog.models import Post
from apps.blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


