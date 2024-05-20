from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.users.models import User
from apps.users.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]