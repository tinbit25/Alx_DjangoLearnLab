from rest_framework import generics, permissions  # Importing the necessary classes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import CustomUser  # Assuming your custom user model is named CustomUser
from rest_framework.permissions import IsAuthenticated  # Permission to ensure user is authenticated

# Follow and Unfollow views using GenericAPIView
class FollowUnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Ensuring that the user is authenticated before proceeding

    def post(self, request, user_id):
        action = request.data.get("action")  # action could be 'follow' or 'unfollow'
        user_to_modify = get_object_or_404(CustomUser, id=user_id)

        if action == 'follow':
            if user_to_modify == request.user:
                return Response({"message": "You cannot follow yourself."}, status=400)
            request.user.following.add(user_to_modify)
            return Response({'message': 'You are now following this user.'})

        elif action == 'unfollow':
            if user_to_modify == request.user:
                return Response({"message": "You cannot unfollow yourself."}, status=400)
            request.user.following.remove(user_to_modify)
            return Response({'message': 'You have unfollowed this user.'})

        return Response({"message": "Invalid action. Use 'follow' or 'unfollow'."}, status=400)
