# In notifications/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='notification_list'),
]
