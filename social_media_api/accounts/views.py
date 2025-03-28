from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.permissions import IsAuthenticated

# To list all users (using GenericAPIView)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()  # Fetch all users from the database
    permission_classes = [IsAuthenticated]  # Ensure that the user is authenticated

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to list all users.
        Returns the list of all users for authenticated users only.
        """
        users = self.get_queryset()
        user_data = [{'id': user.id, 'username': user.username} for user in users]
        return Response(user_data)


# Follow and Unfollow views
@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if user_to_follow == request.user:
        return Response({"message": "You cannot follow yourself."}, status=400)
    request.user.following.add(user_to_follow)
    return Response({'message': 'You are now following this user.'})


@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({'message': 'You have unfollowed this user.'})
