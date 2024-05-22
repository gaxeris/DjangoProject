
from rest_framework import serializers

from apps.blog.models import Category, Post


class PostSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text', 'category']



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
        
class RecentPostsCategorySerializer(CategorySerializer):
    
    recent_posts = serializers.JSONField()
    
    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ['recent_posts']