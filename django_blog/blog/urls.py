# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # View for the list of posts
    path('posts/', views.PostListView.as_view(), name='post_list'),  
    
    # View for creating a new post
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),  # Ensure this is 'posts/new/'
    
    # View for viewing a specific post
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # View for editing a specific post
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # Ensure this is 'posts/<int:pk>/edit/'

    # View for deleting a specific post
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Ensure this is 'posts/<int:pk>/delete/'
]
