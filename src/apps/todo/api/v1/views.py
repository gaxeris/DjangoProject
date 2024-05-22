from urllib import request
from rest_framework import viewsets

from apps.todo.models import TodoItem
from apps.todo.api.v1.serializers import TodoItemSerializer



class TodoItemViewSet(viewsets.ModelViewSet):
    model = TodoItem
    serializer_class = TodoItemSerializer
    
    def get_queryset(self):
        author = self.request.user
        query = TodoItem.objects.filter(owner=author)
        return query
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    