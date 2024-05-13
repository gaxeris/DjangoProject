
from rest_framework import routers



from api.v1.blog.views import CategoryViewSet, PostViewSet
from api.v1.todo.views import TodoItemViewSet


router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

router.register(r'todos', TodoItemViewSet)
