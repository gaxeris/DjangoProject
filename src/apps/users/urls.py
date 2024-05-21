from django.urls import path

from apps.users.views import UserCreateView, UserRetrieveView


urlpatterns = [
    path('signup/', UserCreateView.as_view()),
    path('<int:pk>/', UserRetrieveView.as_view()),
]