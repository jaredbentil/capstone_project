# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views # Import the entire views module

# Create a router
router = DefaultRouter()

# Register our ViewSets with the router
router.register(r'authors', views.AuthorViewSet, basename='author')
router.register(r'books', views.BookViewSet, basename='book')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]





