from django.db import models

from config import settings

# Create your models here.

class TodoItem(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='todo_items')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title