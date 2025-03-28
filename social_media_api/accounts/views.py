from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticate
# Follow and Unfollow functionality
class FollowUnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Ensure this is present to enforce authentication

    def post(self, request, user_id):
        action = request.data.get("action")  # Action could be 'follow' or 'unfollow'
        
        # Fetch the user to follow/unfollow
        user_to_modify = get_object_or_404(CustomUser, id=user_id)

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
