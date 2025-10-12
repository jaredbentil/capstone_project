from rest_framework import serializers
from .models import Customer, Notification, Engineer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'location', 'email', 'last_mile_site', 'service_type']

class NotificationSerializer(serializers.ModelSerializer):
    # This field ensures the engineer's username is shown instead of just the ID
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Notification
        fields = ['id', 'title', 'message', 'is_sent', 'created_by', 'customers', 'sent_at', 'outage_related']

class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = ['id', 'username', 'email']

