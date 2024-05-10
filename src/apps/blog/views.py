
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import OuterRef
from django.db.models.functions import JSONObject

from  django.contrib.postgres.expressions import ArraySubquery

from apps.blog.forms import PostForm
from apps.blog.models import Category, Post

# Create your views here.

def index(request):
    
    recent_posts = Post.objects.order_by('-created_at')

    context = {'recent_posts': recent_posts}
    
    return render(request, 'blog/index.html', context)


def display_all_categories(request):
    
    categories_with_recent_posts = Category.objects.get_recent_posts_per_category()
    
    context = {'categories': categories_with_recent_posts}
    
    return render(request, 'blog/categories.html', context)


def get_post_by_url(request, url):
    
    post = get_object_or_404(Post, slug=url)

    context = {
        'title': post.title,
        'text' : post.text,
        'category': post.category
        }
    
    return render(request, 'blog/single-post.html', context)


def create_new_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('index')
    
    else:
        form = PostForm()
    
 
    return render(request, 'blog/post-form.html', {'form': form})