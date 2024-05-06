from django.shortcuts import get_object_or_404, render
from django.db.models import OuterRef
from django.db.models.functions import JSONObject

from  django.contrib.postgres.expressions import ArraySubquery

from apps.blog.models import Category, Post

# Create your views here.

def index(request):

    """     
    json формата:
    [{name: ..., ..., recent_posts = [{title: ...,}, 
                                      {title: ...,}, {title: ...,}]},..
    ]
    """
    
    recent_posts_subquery = Post.objects.filter(category=OuterRef('pk')).values(
        data = JSONObject(
                title = 'title', text = 'text', slug = 'slug'
        )
    )[:3]

    categories_with_recent_posts = Category.objects.annotate(
        recent_posts = ArraySubquery(recent_posts_subquery)
    ).values('name', 'description', 'slug', 'recent_posts')
        
    
    """    
    deprecated
    расширение для Manager записанного в objects модели
    использовалось до миграции на постгрес и выражения ArraySubquery
    
    recent_posts_per_category = Post.objects.get_3_recent_posts_per_category()
    
    print(recent_posts_per_category)
    """
    
    context = {'categories': categories_with_recent_posts}
    
    return render(request, 'blog/index.html', context)


def display_all_categories(request):
    
    categories_query = Category.objects.all()
    
    context = {'categories': categories_query}
    
    return render(request, 'blog/categories.html', context)


def get_post_by_url(request, url):
    
    post = get_object_or_404(Post, slug=url)

    context = {
        'title': post.title,
        'text' : post.text,
        }
    
    return render(request, 'blog/single-post.html', context)