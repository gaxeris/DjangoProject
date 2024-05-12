from rest_framework import viewsets

from apps.todo.models import TodoItem
from apps.todo.serializers import TodoItemSerializer



class TodoItemViewSet(viewsets.ModelViewSet):
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    