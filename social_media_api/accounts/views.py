from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser 

# Serializer for CustomUser 
class CustomUser Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ['id', 'username', 'email']  # Include other fields as necessary

# View to list all users
class UserListView(generics.ListAPIView):
    queryset = CustomUser .objects.all()  # This satisfies the requirement for CustomUser .objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access this view
    serializer_class = CustomUser Serializer  # Use the serializer created above

# View to follow/unfollow users
class FollowUnfollowUser View(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Enforces that only authenticated users can follow/unfollow

    def post(self, request, user_id):
        action = request.data.get("action")  # Action could be 'follow' or 'unfollow'
        
        # Fetch the user to follow/unfollow
        user_to_modify = get_object_or_404(CustomUser , id=user_id)

        # Follow logic
        if action == 'follow':
            if user_to_modify == request.user:
                return Response({"message": "You cannot follow yourself."}, status=400)
            request.user.following.add(user_to_modify)  # Add to following relationship
            return Response({'message': 'You are now following this user.'})

        # Unfollow logic
        elif action == 'unfollow':
            if user_to_modify == request.user:
                return Response({"message": "You cannot unfollow yourself."}, status=400)
            request.user.following.remove(user_to_modify)  # Remove from following relationship
            return Response({'message': 'You have unfollowed this user.'})

        return Response({"message": "Invalid action. Use 'follow' or 'unfollow'."}, status=400)

# Ensure to add the necessary URL routing in your urls.py