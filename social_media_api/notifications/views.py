from django.shortcuts import render

# Create your views here.


from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    List all notifications for the current user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.notifications.all()

class MarkNotificationsAsReadView(APIView):
    """
    Mark all unread notifications for the current user as read.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.notifications.filter(unread=True).update(unread=False)
        return Response(status=status.HTTP_204_NO_CONTENT)