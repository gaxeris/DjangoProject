
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.blog.api.v1.serializers import PostSerializer
from apps.blog.models import Category, Post
from apps.users.models import User


client = APIClient()


class PostViewSetTest(TestCase): 
    def setUp(self) -> None:
        self.user = User.objects.create(
            username = 'author',
            password = 'author'
        )
        self.user.save()
        
        self.category = Category.objects.create(
            name='Testing',
            description='Its a category to test out some features'
        )
        self.category.save()
        
        self.post1 = Post.objects.create(
            author = self.user,
            title='The oldest post',
            text='This post was created as the 1st',
            category=self.category
        )
        self.post2 = Post.objects.create(
            author = self.user,
            title='The "middle" post',
            text='This one was created as the 2nd',
            category=self.category
        )
        self.post3 = Post.objects.create(
            author = self.user,
            title='The earliest post',
            text='This one was created as the 3d',
            category=self.category
        )
        
        
    def test_get_list(self):  
        response = client.get(reverse('blog:post-list'))
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


    def test_get_single_post(self):
        pk1 = self.post1.pk
        post = Post.objects.get(pk=pk1)
        serializer = PostSerializer(post, many=False)
        
        response = client.get(reverse('blog:post-detail', args=(pk1,))) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        client.force_authenticate(user=self.user)
        response = client.get(reverse('blog:post-detail', args=(pk1,))) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
        invalid_id = 666
        response = client.get(reverse('blog:post-detail', args=(invalid_id,))) 
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        client.force_authenticate(user=None)
        
    
    def test_post_single_post(self):
        valid_post_data = {
            'title': 'The new post',
            'text': 'This one is created as the 4th',
            'category': self.category.pk
        }
        invalid_post_data = {
            'title': 'This post shouldnt be created',
            'text': 'This one tries to be created as the 5th',
            'category': 'Invalid foreign key field'
        }
         
        response = client.post(
            reverse('blog:post-list'),
            data=valid_post_data,
            format='json',
        ) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        client.force_authenticate(user=self.user)
        response = client.post(
            reverse('blog:post-list'),
            data=valid_post_data,
            format='json'
        ) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = client.post(
            reverse('blog:post-list'),
            data=invalid_post_data,
            format='json',
        ) 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        client.force_authenticate(user=None)
    
    
    def test_autofilled_author_when_posting(self):
        valid_post_data = {
            'title': 'The new post',
            'text': 'This one is created as the 4th',
            'category': self.category.pk,
        }
        
        client.force_authenticate(user=self.user)
        response = client.post(
            reverse('blog:post-list'),
            data=valid_post_data,
            format='json',
        ) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        new_post = Post.objects.get(title='The new post')
        autofilled_author_field = new_post.author
        self.assertEqual(autofilled_author_field, self.user)
        
        client.force_authenticate(user=None)
        
    
    def test_modify_only_owned_post(self):
        temp_user = User.objects.create(
            username = 'not_an_author',
            password = 'pass',
        )
        temp_user.save()

        pk1 = self.post1.pk
        new_text = 'This was modified by PATCH'
        patch_data = {
            'text': new_text,
        }
        
        client.force_authenticate(user=temp_user)
        response = client.patch(
            reverse('blog:post-detail', args=(pk1,)),
            data=patch_data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        client.force_authenticate(user=None)
        
        client.force_authenticate(user=self.user)
        response = client.patch(
            reverse('blog:post-detail', args=(pk1,)),
            data=patch_data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.force_authenticate(user=None)
        
        patched_post = Post.objects.get(pk=pk1)
        patched_data = patched_post.text
        self.assertEqual(patched_data, new_text)