from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Todo serializer
class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested user serializer

    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'description', 'completed', 'created_at', 'updated_at']
