from django.contrib import admin

from apps.blog.models import Category, Post

# Register your models here.


# генерация slug при создании записей в админке на основе наименований
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
