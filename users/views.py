from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer, UserCreateSerializer
import logging

logger = logging.getLogger(__name__)


class HomeListView(ListView):
    """Renders the home page with a list of users."""
    model = CustomUser
    context_object_name = "user_list"
    template_name = "users/home.html"



class RegisterUserView(APIView):
    """API view for user registration."""
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"New user registered: {serializer.data['username']}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"Registration failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    """API view for listing all users."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            users = CustomUser.objects.all()
            serializer = UserSerializer(users, many=True)
            logger.info(f"Retrieved {len(users)} users")
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")
            return Response(
                {"error": "Failed to retrieve users"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserDetailView(APIView):
    """API view for retrieving, updating, and deleting individual users."""
    permission_classes = [IsAuthenticated]

    def get_user(self, pk):
        """Helper method to get a user by primary key."""
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return None

    def get(self, request, pk):
        user = self.get_user(pk)
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_user(pk)
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"User {pk} updated successfully")
            return Response(serializer.data)
        logger.warning(f"User update failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_user(pk)
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        logger.info(f"User {pk} deleted successfully")
        return Response(status=status.HTTP_204_NO_CONTENT)

class LogoutView(APIView):
    """API view for user logout."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            logger.info(f"User {request.user.username} logged out successfully")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except KeyError:
            logger.warning("Logout failed: No refresh token provided")
            return Response(
                {'error': 'Refresh token is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Logout error: {str(e)}")
            return Response(
                {'error': 'Invalid token'},
                status=status.HTTP_400_BAD_REQUEST
            )
