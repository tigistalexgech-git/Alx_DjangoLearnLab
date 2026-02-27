from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegisterSerializer

User = get_user_model()

@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return Response({"message": "Followed"})

@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({"message": "Unfollowed"})


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=400)

# Create your views here.
