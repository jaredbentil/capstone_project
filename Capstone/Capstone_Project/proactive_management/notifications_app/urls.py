from django.urls import path, include 
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Register viewsets with the router
router.register(r'customers', views.CustomerViewSet, basename='customer')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'engineers', views.EngineerViewSet, basename='engineer')

# URL patterns
urlpatterns = router.urls 
urlpatterns = [
    *router.urls,
    path('login/', obtain_auth_token, name='api_token_auth'),
]
