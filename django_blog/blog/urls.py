# blog/urls.py or blog/users/urls.py

from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
]
