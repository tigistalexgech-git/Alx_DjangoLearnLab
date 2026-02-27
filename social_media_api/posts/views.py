from django.shortcuts import render
from rest_framework import generics,viewsets, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    Like.objects.get_or_create(post=post, user=request.user)
    return Response({"message": "Liked"})

@api_view(['POST'])
def unlike_post(request, pk):
    post = Post.objects.get(pk=pk)
    Like.objects.filter(post=post, user=request.user).delete()
    return Response({"message": "Unliked"})

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
