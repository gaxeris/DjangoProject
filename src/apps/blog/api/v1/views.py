from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from apps.blog.api.v1.permissions import BlogPostCustomPermission
from apps.blog.models import Category, Post
from apps.blog.api.v1.serializers import (
    AuthorPostsSerializer,
    CategorySerializer,
    PostSerializer,
    RecentPostsCategorySerializer,
)
from apps.users.models import User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (BlogPostCustomPermission,)

    @action(detail=False, url_path="recent")
    def get_recent_posts(self, request):
        ordered_query = self.get_queryset().order_by("-created_at")
        serializer = self.get_serializer(ordered_query, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.action == "get_recent_posts_per_category":
            return RecentPostsCategorySerializer

        return super().get_serializer_class()

    @action(detail=False, url_path="recent-per-category")
    def get_recent_posts_per_category(self, request):
        result_categories = Category.objects.get_recent_posts_per_category()

        serializer = self.get_serializer(result_categories, many=True)
        return Response(serializer.data)


class AuthorsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthorPostsSerializer
