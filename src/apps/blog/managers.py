from django.apps import apps
from django.db import models
from django.db.models import OuterRef
from django.db.models.functions import JSONObject

from django.contrib.postgres.expressions import ArraySubquery


class PostManager(models.Manager):
    """Manager for Post model that contains extra subquery method for Category\`s manager"""

    def get_recent_posts_per_category_subquery(self):
        """Returns subquery of recent posts based on the foreign key in the field category.

        This method is intended to be used by Category\`s manager.
        Returns subquery of three recent posts in a required category in descending order with
        JSONObject field.\n
        Return format: [{"title":..., "text":..., "slug":...}, {...}, {...}]
        """
        recent_posts_subquery = (
            self.filter(category=OuterRef("pk"))
            .values(data=JSONObject(title="title", text="text", slug="slug"))
            .order_by("-created_at")[:3]
        )

        return recent_posts_subquery


class CategoryManager(models.Manager):
    """Custom manager that contains extra get_recent_posts_per_category() method"""

    def get_recent_posts_per_category(self):
        """Returns categories with the list of recent posts in them.

        This method uses custom Post\`s manager method.
        Returns queryset of categories with annotaded field named "recent_posts", which
        contains list of JSONObjects with Post object each.\n
        Return format: [{"name":..., "description":..., "slug":...,\n
                        "recent_posts":[{"title":..., "text":..., "slug":...}, {...}, {...}]},\n
                        {"name":..., "description":...}, {...}, ...]

        """
        recent_posts_subquery = apps.get_model(
            "blog", "Post"
        ).objects.get_recent_posts_per_category_subquery()

        result_query = self.annotate(
            recent_posts=ArraySubquery(recent_posts_subquery)
        ).values("name", "description", "slug", "recent_posts")

        return result_query
