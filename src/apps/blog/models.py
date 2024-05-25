from django.db import models
from django.utils.text import slugify

from apps.blog.managers import CategoryManager, PostManager
from django.conf import settings


# Create your models here.


class Category(models.Model):
    """This model uses extended model manager"""

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    slug = models.SlugField(unique=True)

    objects = CategoryManager()

    def __str__(self):
        return self.name


class Post(models.Model):
    """This model uses custom model manager and
    has a method to generate unique slugs on save() based on Post\`s name"""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="written_posts",
        null=True,
    )

    title = models.CharField(max_length=150)
    text = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True)

    # base manager eхtension
    objects = PostManager()

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}{num}"
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = self.get_unique_slug()

        super(Post, self).save(*args, **kwargs)
