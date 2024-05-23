
from rest_framework import serializers

from apps.blog.models import Category, Post
from apps.users.models import User



class PostSerializer(serializers.ModelSerializer):  
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = [
            'id',
            'category',
            'author',
            'title',
            'text',
        ]



class CategorySerializer(serializers.ModelSerializer):   
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
   
        
class RecentPostsCategorySerializer(CategorySerializer):    
    recent_posts = serializers.JSONField()
    
    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ['recent_posts']
        
        

class AuthorPostsSerializer(serializers.ModelSerializer): 
    written_posts = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Post.objects.all()
    )
    
    class Meta:
        model = User
        fields = ['id', 'username', 'written_posts']
