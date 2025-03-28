from django.urls import path
from . import views

urlpatterns = [
    # Blog post URLs
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # View a specific post
    path('posts/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_new'),  # Create a new comment

    # Comment update and delete URLs
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),  # Edit an existing comment
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),  # Delete a comment
]
