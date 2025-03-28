from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser 
from rest_framework.permissions import IsAuthenticated

class FollowUnfollowUser View(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        action = request.data.get("action")
        user_to_modify = get_object_or_404(CustomUser , id=user_id)

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

class UserListView(generics.ListAPIView):
    queryset = CustomUser .objects.all()  # This will satisfy the requirement for CustomUser .objects.all()
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this view
    serializer_class = CustomUser Serializer  # You need to create a serializer for CustomUser 

# Make sure to create a serializer for CustomUser 
from rest_framework import serializers

class CustomUser Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ['id', 'username', 'email']  # Add other fields as necessary