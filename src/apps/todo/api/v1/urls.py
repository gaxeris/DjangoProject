
from rest_framework import routers
from django.urls import path

from apps.todo.api.v1.views import TodoItemViewSet


router_todo = routers.DefaultRouter()

router_todo.register(r'todos', TodoItemViewSet, basename='todo')


