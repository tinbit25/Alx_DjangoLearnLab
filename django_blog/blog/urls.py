from django.urls import path
from . import views

urlpatterns = [
    # Post URLs
     path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post_by_tag'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # View a specific post

    # Comment related URLs
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_new'),  # Create a new comment
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),  # Update a comment
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),  # Delete a comment
]
