from django.contrib.auth.models import User
from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Todo
from .serializers import TodoSerializer, UserSerializer

# User registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Hash password automatically
        return user

# User registration view
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]  # Publicly accessible

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Todo viewset
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        # Only return todos for the authenticated user
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the authenticated user to the todo
        serializer.save(user=self.request.user)
