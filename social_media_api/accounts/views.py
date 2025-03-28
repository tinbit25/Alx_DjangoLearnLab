from rest_framework import generics, permissions  # Ensure these are imported
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated

# Follow and Unfollow views using GenericAPIView
class FollowUnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Ensures the user is authenticated before proceeding

    def post(self, request, user_id):
        action = request.data.get("action")  # Action could be 'follow' or 'unfollow'
        user_to_modify = get_object_or_404(CustomUser, id=user_id)  # Get the user to follow/unfollow

        if action == 'follow':
            if user_to_modify == request.user:
                return Response({"message": "You cannot follow yourself."}, status=400)
            request.user.following.add(user_to_modify)  # Add to following relationship
            return Response({'message': 'You are now following this user.'})

        elif action == 'unfollow':
            if user_to_modify == request.user:
                return Response({"message": "You cannot unfollow yourself."}, status=400)
            request.user.following.remove(user_to_modify)  # Remove from following relationship
            return Response({'message': 'You have unfollowed this user.'})

        return Response({"message": "Invalid action. Use 'follow' or 'unfollow'."}, status=400)

# Optionally: To get a list of all users (useful for testing or general API functionality)
class ListAllUsersView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = CustomUser.objects.all()  # Retrieve all users
        user_data = [{"id": user.id, "username": user.username} for user in users]  # Format the data as needed
        return Response({"users": user_data})
