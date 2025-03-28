# In notifications/models.py

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser  # User model
from posts.models import Post  # Assuming posts are the target of notifications

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(CustomUser, related_name='created_notifications', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)  # Description of the action, e.g., 'liked your post'
    target_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Model type of the target
    target_id = models.PositiveIntegerField()  # ID of the target
    target = GenericForeignKey('target_ct', 'target_id')  # Can point to a Post, Comment, etc.
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # Indicates if the notification has been read

    def __str__(self):
        return f"Notification: {self.verb} by {self.actor} for {self.recipient}"
