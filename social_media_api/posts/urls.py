from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
]
# In posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/like/', views.LikePostView.as_view(), name='like_post'),
    path('<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike_post'),
]
