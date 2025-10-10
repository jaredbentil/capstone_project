# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

CustomUser = get_user_model()

CustomUser = get_user_model().objects.create_user

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the CustomUser model, used for retrieving user details."""
    class Meta:
        model = get_user_model() # Using get_user_model() directly here
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'followers', 'following')
        read_only_fields = ('followers', 'following')

class RegisterSerializer(serializers.ModelSerializer):
    
    serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = get_user_model() # Using get_user_model() directly here
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        """
        Check that the two password entries match.
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return data

    def create(self, validated_data):
        """
        Create a new user and a corresponding auth token.
        """
       
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )

        Token.objects.create(user=user)
        
        return user