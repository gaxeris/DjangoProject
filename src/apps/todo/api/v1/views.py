from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.todo.models import TodoItem
from apps.todo.api.v1.serializers import TodoItemSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    """ViewSet that provides every HTTP method for TodoItems model

    Its queryset provides items only to the authorized users and only those objects
    that are owned by said users.
    When 'post'-ing new ToDo item, this viewset autofills TodoItem.owner field with
    a correct value.
    """

    model = TodoItem
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        author = self.request.user
        query = TodoItem.objects.filter(owner=author)
        return query

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
