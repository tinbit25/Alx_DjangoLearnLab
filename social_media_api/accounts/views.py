from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserRegistrationSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], 
                                password=serializer.validated_data['password'])
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def get_object(self):
        return self.request.user
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
