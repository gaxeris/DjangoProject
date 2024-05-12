from django.contrib import admin

from apps.todo.models import TodoItem

# Register your models here.
admin.site.register(TodoItem)