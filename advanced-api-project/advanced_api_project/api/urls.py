from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
# Register AuthorViewSet at /authors/
router.register(r'authors', views.AuthorViewSet)
# Register BookViewSet at /books/
router.register(r'books', views.BookViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # Include all paths managed by the router (e.g., authors/, books/, etc.)
    path('', include(router.urls)),
]
# Additional custom endpoints can be added here if needed.


