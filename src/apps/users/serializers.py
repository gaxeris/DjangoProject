
from rest_framework import serializers

from apps.blog.models import Post
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    
    written_posts = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Post.objects.all()
    )
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'written_posts']
        extra_kwargs = {'password': {'write_only': True}}
