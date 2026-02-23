from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostSearchView,
    PostByTagListView,
)

uurlpatterns = [
   path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    # path(
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),

    # update a comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),

    # delete a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
    path('search/', PostSearchView.as_view(), name='post_search'),
]
