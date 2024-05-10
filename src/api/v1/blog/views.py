

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.blog.models import Category, Post
from apps.blog.serializers import CategorySerializer, PostSerializer, RecentPostsCategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
    def get_serializer_class(self):
        
        if self.action == 'get_recent_posts_per_category':
            return RecentPostsCategorySerializer
        
        return super().get_serializer_class()


    @action(detail=False, url_path='recent')
    def get_recent_posts_per_category(self, request):
        
        result_categories = Category.objects.get_recent_posts_per_category()

        serializer = self.get_serializer(result_categories, many=True)
        return Response(serializer.data)    

