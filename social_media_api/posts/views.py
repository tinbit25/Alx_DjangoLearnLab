# In posts/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures that only authenticated users can like

    def post(self, request, pk):
        # Retrieve the post or return 404 if not found
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # Create or get the Like object for the user and post (prevents duplicate likes)
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post owner
        notification = Notification.objects.create(
            recipient=post.author,  # Assuming Post model has an 'author' field
            actor=user,
            verb="liked your post",
            target=post,
            target_ct=ContentType.objects.get_for_model(post),
        )

        return Response({"message": "Post liked successfully.", "notification": str(notification)}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures that only authenticated users can unlike

    def post(self, request, pk):
        # Retrieve the post or return 404 if not found
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if the user has liked the post, and if so, delete the like
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"message": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the like
        like.delete()

        # Optionally, delete the corresponding notification
        Notification.objects.filter(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post
        ).delete()

        return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
