from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, ProfileSerializer

# Use the custom user model
User = get_user_model()

# Register a new user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Login view (stub)
class LoginView(generics.GenericAPIView):
    def post(self, request):
        return Response({"message": "Login endpoint - implement authentication logic"}, status=status.HTTP_200_OK)

# View user profile
class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# Follow user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        return Response({"message": f"You followed user {user_id}"}, status=status.HTTP_200_OK)

# Unfollow user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        return Response({"message": f"You unfollowed user {user_id}"}, status=status.HTTP_200_OK)
