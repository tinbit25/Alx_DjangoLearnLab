from django.urls import path
from . import views

urlpatterns = [
    path('follow_unfollow/<int:user_id>/', views.FollowUnfollowUserView.as_view(), name='follow_unfollow_user'),
    path('users/', views.ListAllUsersView.as_view(), name='list_all_users'),  # Optional for testing
]
