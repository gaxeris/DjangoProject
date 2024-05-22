from django.contrib import admin

from apps.blog.models import Category, Post

# Register your models here.

# генерация url при создании записей в админке
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
