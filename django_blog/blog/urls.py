from django.urls import path
from . import views

urlpatterns = [
    # Blog post URLs
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # View a specific post

    # Comment related URLs
    path('posts/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_new'),  # Create a new comment
    path('comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),  # Update a comment
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),  # Delete a comment
]
