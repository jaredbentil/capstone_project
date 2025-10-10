

from contextvars import Token
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status, generics, mixins
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from .serializers import UserSerializer, RegisterSerializer


CustomUser = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    Returns user data and an auth token upon successful registration.
    """
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # We only return the user data now, no token.
        return Response(
            UserSerializer(user, context=self.get_serializer_context()).data,
            status=status.HTTP_201_CREATED
        )

class CustomAuthToken(ObtainAuthToken):
    """
    API endpoint for user login.
    Extends DRF's ObtainAuthToken to return user data alongside the token.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class UserProfileView(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      generics.GenericAPIView):
    """
    API endpoint for retrieving and updating the authenticated user's profile.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Returns the authenticated user's object
        return self.request.user

    def get(self, request, *args, **kwargs):
        """Handle GET requests to retrieve the user profile."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Handle PUT requests to update the user profile."""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Handle PATCH requests to partially update the user profile."""
        return self.partial_update(request, *args, **kwargs)

    

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    It also includes custom `follow` and `unfollow` actions.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], url_path='follow')
    def follow(self, request, pk=None):
        """Action to follow a user."""
        user_to_follow = self.get_object()
        current_user = request.user

        if user_to_follow == current_user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        current_user.following.add(user_to_follow)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'], url_path='unfollow')
    def unfollow(self, request, pk=None):
        """Action to unfollow a user."""
        user_to_unfollow = self.get_object()
        current_user = request.user
        
        current_user.following.remove(user_to_unfollow)
        return Response(status=status.HTTP_204_NO_CONTENT)