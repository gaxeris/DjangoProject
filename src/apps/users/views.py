from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.users.models import User
from apps.users.permissions import UserIsSelfPermission
from apps.users.serializers import (
    UserImageSerializer,
    UserLoginSignupSerializer,
    UserSerializer,
)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSignupSerializer
    permission_classes = [AllowAny]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserSetImageView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserImageSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        image_file = self.request.FILES["image"]
        serializer = UserImageSerializer(
            instance=instance,
            data=request.data,
            context={"image_file": image_file},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response("Upload Started...")

    def put(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)
