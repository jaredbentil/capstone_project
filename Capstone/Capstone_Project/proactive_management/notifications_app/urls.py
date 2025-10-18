from django.urls import path

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'notifications', views.NotificationViewSet)
router.register(r'engineers', views.EngineerViewSet)

urlpatterns = router.urls


