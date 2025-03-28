# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # View for the list of posts
    path('posts/', views.PostListView.as_view(), name='post_list'),  
    
    # View for creating a new post
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Exact path for creating a new post
    
    # View for viewing a specific post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # View for editing a specific post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_edit'),  # Exact path for editing a post

    # View for deleting a specific post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Exact path for deleting a post

 path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
