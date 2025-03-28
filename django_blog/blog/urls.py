# blog/urls.py or blog/users/urls.py

from django.urls import path
from . import views  # Import views

app_name = 'blog'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
  path('', views.PostListView.as_view(), name='post_list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),  # Correct path for creating posts
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # Correct path for post detail
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # Correct path for editing posts
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Correct path for deleting posts
]
