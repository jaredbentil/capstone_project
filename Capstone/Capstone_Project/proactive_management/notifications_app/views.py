from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer, NotificationSerializer, EngineerSerializer
from .models import Customer, Notification, Engineer
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Customer instances.
    """
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class NotificationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Notification instances.
    """
    
    queryset = Notification.objects.all().order_by('-timestamp')
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

class EngineerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing Engineer instances.
    """
    queryset = Engineer.objects.all().order_by('username')
    serializer_class = EngineerSerializer
    permission_classes = [IsAuthenticated]