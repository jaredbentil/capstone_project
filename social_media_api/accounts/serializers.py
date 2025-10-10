# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the CustomUser model, used for retrieving user details."""
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'followers', 'following')
        read_only_fields = ('followers', 'following')

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Includes password confirmation and uses the create_user manager method.
    """
    # Explicitly adding a password confirmation field.
    # It is write_only, so it will be used for validation but not shown in the API output.
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
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
        Create and return a new user, using the create_user method.
        """
        # Using the improved create_user method which handles password hashing.
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user