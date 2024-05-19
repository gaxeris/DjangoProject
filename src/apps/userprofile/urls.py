from django.urls import path

from apps.userprofile.views import UserProfileCreateView


urlpatterns = [
    path('signup/', UserProfileCreateView.as_view()),
]
