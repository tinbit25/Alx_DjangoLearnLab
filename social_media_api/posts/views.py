from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

# View for liking a post
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that the user is authenticated

    def post(self, request, pk):
        # Safely retrieve the Post object or return a 404 error if not found
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # Create a like object or retrieve the existing one to prevent duplicate likes
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post's author
        notification = Notification.objects.create(
            recipient=post.author,  # Assuming the post has an 'author' field
            actor=user,
            verb="liked your post",
            target=post,
            target_ct=ContentType.objects.get_for_model(post),
        )

        # Return a success response along with notification details
        return Response({"message": "Post liked successfully.", "notification": str(notification)}, status=status.HTTP_201_CREATED)


# View for unliking a post
class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure that the user is authenticated

    def post(self, request, pk):
        # Safely retrieve the Post object or return a 404 error if not found
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # Find the like object to delete
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"message": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like object
        like.delete()

        # Optionally, remove the corresponding notification
        Notification.objects.filter(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post
        ).delete()

        return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
