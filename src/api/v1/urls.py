from atexit import register
from rest_framework import routers

from api.v1.blog.views import CategoryViewSet, PostViewSet


router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
