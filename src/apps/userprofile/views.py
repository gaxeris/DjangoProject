from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.userprofile.models import UserProfile
from apps.userprofile.serializers import UserProfileSerializer


class UserProfileCreateView(generics.CreateAPIView):
    
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]