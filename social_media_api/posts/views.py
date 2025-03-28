# In posts/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        # Check if user has already liked the post
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the like
        Like.objects.create(user=user, post=post)

        # Create a notification for the post owner
        notification = Notification.objects.create(
            recipient=post.author,  # assuming Post model has an `author` field
            actor=user,
            verb="liked your post",
            target=post,
            target_ct=ContentType.objects.get_for_model(post),
        )

        return Response({"message": "Post liked successfully.", "notification": str(notification)}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        # Check if the user has liked the post
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"message": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the like
        like.delete()

        # Optionally, you can also delete the notification if necessary
        Notification.objects.filter(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post
        ).delete()

        return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
