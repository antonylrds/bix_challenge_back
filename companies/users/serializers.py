from uuid import uuid4
from rest_framework import serializers

from .models import CustomUser as User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex_verbose', default=uuid4)
    class Meta:
        model = User
        fields = ['id','email', 'password']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)