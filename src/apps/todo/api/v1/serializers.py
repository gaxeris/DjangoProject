from rest_framework import serializers

from apps.todo.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    """TodoItem serializer that should be used by default"""

    class Meta:
        model = TodoItem
        fields = [
            "id",
            "title",
            "description",
            "is_completed",
        ]
