from django.apps import apps
from django.db import models
from django.db.models import OuterRef
from django.db.models.functions import JSONObject

from  django.contrib.postgres.expressions import ArraySubquery




class PostManager(models.Manager):
    
    
    def get_recent_posts_per_category_subquery(self):
        
    #    query_set = self.get_queryset
        
        recent_posts_subquery = self.filter(category=OuterRef('pk')).values(
            data = JSONObject(
                    title = 'title', text = 'text', slug = 'slug'
            )
        ).order_by('-created_at')[:3]
        
        return recent_posts_subquery
        
        
class CategoryManager(models.Manager):
    
    def get_recent_posts_per_category(self):
        
        #query_set = self.get_queryset()
        
        recent_posts_subquery = apps.get_model('blog','Post').objects.get_recent_posts_per_category_subquery()
        
        result_query = self.annotate(
            recent_posts = ArraySubquery(recent_posts_subquery)
        ).values('name', 'description', 'slug', 'recent_posts')
        
        return result_query
