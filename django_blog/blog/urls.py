from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
     path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
     path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post_by_tag'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # View a specific post

    # Comment related URLs
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_new'),  # Create a new comment
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),  # Update a comment
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),  # Delete a comment
]
