
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, CustomAuthToken, UserProfileView, UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('', include(router.urls)), # Include the router URLs
    path('follow/<int:user_id>/', UserViewSet.as_view({'post': 'follow'}), name='follow-user'),
    path('unfollow/<int:user_id>/', UserViewSet.as_view({'post': 'unfollow'}), name='unfollow-user'),
]