from rest_framework import routers
from django.urls import path

from apps.todo.api.v1.views import TodoItemViewSet


router_todo = routers.DefaultRouter()

app_name = "todo"
router_todo.register(r"", TodoItemViewSet, basename="todo")
