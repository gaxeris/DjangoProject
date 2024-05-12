

from rest_framework import serializers

from apps.todo.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TodoItem
        fields = [
            'id',
            'title',
            'description',
            'is_completed'
        ]