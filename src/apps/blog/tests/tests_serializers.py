



from django.test import TestCase

from apps.blog.api.v1.serializers import PostSerializer
from apps.blog.models import Category, Post
from apps.users.models import User



class PostSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create(
            username = 'temp_user',
            password = 'temp_user'
        )
        cls.user.save()
        
        cls.category = Category.objects.create(
            name='Gamedev',
            description='There are some news about gamedev in this category'
        )
        cls.category.save()
        
        cls.post = Post.objects.create(
            author = cls.user,
            title='LoL',
            text='Have you seen that riot want to add Vanguard to the game?',
            category=cls.category
        )
        
        cls.serializer = PostSerializer(instance=cls.post)
        
        
    def test_serializer_is_valid(self):    
        data = self.serializer.data
        serializer = PostSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        
    def test_serializer_expected_fields(self):
        data = self.serializer.data
        expected_fields = {
            'id',
            'category',
            'author',
            'title',
            'text',
        }
        self.assertEqual(set(data.keys()), expected_fields)
        