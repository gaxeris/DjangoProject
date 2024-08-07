from django.urls import path

from apps.users.views import (
    UserCreateView,
    UserListView,
    UserRetrieveView,
    UserSetImageView,
)


app_name = "users"
urlpatterns = [
    path("signup/", UserCreateView.as_view()),
    path("<int:pk>/", UserRetrieveView.as_view()),
    path("<int:pk>/image/", UserSetImageView.as_view()),
    path("", UserListView.as_view()),
]
