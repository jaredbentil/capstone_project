

from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.StringRelatedField() # Shows a string representation of the target object

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'unread', 'timestamp']