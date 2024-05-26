from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.users.models import User
from apps.users.permissions import UserCustomPermission
from apps.users.serializers import UserLoginSignupSerializer, UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSignupSerializer
    permission_classes = [AllowAny]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveView(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, UserCustomPermission]
