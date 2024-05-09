from django.urls import path
from apps.blog import views

app_name = 'apps.blog'

urlpatterns = [
    path('', views.index, name='blog'),
    path('categories/', views.display_all_categories, name='categories'),
    path('posts/<slug:url>/', views.get_post_by_url, name='single-post'),
    path('posts/create', views.create_new_post)
]