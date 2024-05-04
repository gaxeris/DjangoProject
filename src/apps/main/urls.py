from django.urls import path
from apps.main import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
]
