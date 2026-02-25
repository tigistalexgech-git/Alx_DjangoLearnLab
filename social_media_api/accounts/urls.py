from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileView, LoginView
from .views import follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', obtain_auth_token),
    path('profile/', ProfileView.as_view()),
    path('follow/<int:user_id>/', follow_user),
    path('unfollow/<int:user_id>/', unfollow_user),
]