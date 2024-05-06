from django.db import models


class PostManager(models.Manager):
    
    def get_3_recent_posts_per_category(self):
        
        from apps.blog.models import Category
        all_categories = Category.objects.all()
        
        query_set = self.get_queryset()
        result_query = query_set.none()
        
        for category in all_categories:
            result_query = result_query.union(
                query_set.filter(category=category)
                .order_by('-created_at')
                [:3]
            )
        
        return result_query.order_by('category', '-created_at')