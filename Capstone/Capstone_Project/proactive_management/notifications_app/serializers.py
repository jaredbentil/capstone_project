from rest_framework import serializers
from .models import Customer, Notification, Engineer
from django.db import transaction

# --- CUSTOMER SERIALIZER ---
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'location', 'email', 'last_mile_site', 'service_type']


# --- NOTIFICATION SERIALIZER ---
class NotificationSerializer(serializers.ModelSerializer):
    # Read-only field to show the username instead of the engineer's ID
    created_by = serializers.ReadOnlyField(source='created_by.username')
    
    # Custom field to display a list of customer names (read-only for GET requests)
    customer_names = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        
        fields = [
            'id', 'subject', 'message_body', 'status', 'outage_related', 
            'is_planned_maintenance', 'is_root_cause_analysis', 
            'created_by', 'customers', 'customer_names', 'timestamp', 'sent_at'
        ]
        # Allow 'customers' to be optional since a notification can be a draft first
        extra_kwargs = {
            'customers': {'required': False}
        }
        # These fields are set by the system/views, not by API input
        read_only_fields = ['status', 'timestamp', 'sent_at'] 

    def get_customer_names(self, obj):
        """Returns a list of customer names for a GET request."""
        return [customer.name for customer in obj.customers.all()]


# --- ENGINEER (USER) SERIALIZER ---
class EngineerSerializer(serializers.ModelSerializer):
    # CRITICAL FIX: Add write_only=True to password for security
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Engineer
        fields = ['id', 'username', 'email', 'password']
        # Optional: Set required=False for email if it's not strictly mandatory
        extra_kwargs = {
            'email': {'required': False}
        }


    @transaction.atomic
    def create(self, validated_data):
        # Ensures password is hashed using Django's create_user method
        user = Engineer.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
    
    @transaction.atomic
    def update(self, instance, validated_data):
        # Pop password first to handle it separately
        password = validated_data.pop('password', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        if password:
            instance.set_password(password) # Hashes the new password
            
        instance.save()
        return instance