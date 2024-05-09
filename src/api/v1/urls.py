from atexit import register
from rest_framework import routers

from api.v1.blog.views import PostViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)