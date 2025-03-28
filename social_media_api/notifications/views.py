# In notifications/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch unread notifications for the current user
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        
        # Mark them as read
        notifications.update(read=True)

        # Serialize and return the notifications
        notifications_data = [{'actor': notif.actor.username, 'verb': notif.verb, 'timestamp': notif.timestamp} for notif in notifications]
        
        return Response({"notifications": notifications_data})
