from django.urls import path, include 
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# FIX: Explicitly set basename for each ViewSet
router.register(r'customers', views.CustomerViewSet, basename='customer')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'engineers', views.EngineerViewSet, basename='engineer')

urlpatterns = router.urls 
# Note: You need the 'login/' path in the project's urls.py, which you already did.
# Final URL Pattern list
urlpatterns = [
    *router.urls,
    path('login/', obtain_auth_token, name='api_token_auth'),
]
