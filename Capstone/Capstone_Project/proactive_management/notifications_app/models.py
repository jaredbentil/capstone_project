from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

class Engineer(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='engineer_groups', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='engineer_permissions', 
        blank=True
    )

class Meta:
    verbose_name = 'Engineer'
    verbose_name_plural = 'Engineers'
    
def __str__(self):
    return self.username

class Customer(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    last_mile_site = models.CharField(max_length=255, help_text="e.g., street address or specific site name")
    service_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Notification(models.Model):
    """
    Stores all communication events (notifications).
    """
    
    # Using settings.AUTH_USER_MODEL is the standard practice for 
    # referencing your custom user model (Engineer).
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, # Changed from CASCADE to SET_NULL for safety
        null=True,
        related_name='notifications_created',
        verbose_name='Creating Engineer'
    )
    
    subject = models.CharField(max_length=255) # Title from your first attempt
    message_body = models.TextField() # Message from your first attempt
    
    # Many-to-Many relationship for targeted sending
    customers = models.ManyToManyField(
        Customer,
        related_name='notifications_received', 
        blank=True
    )
    
    is_sent = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True) # created_at/timestamp
    sent_at = models.DateTimeField(null=True, blank=True)
    
    # Boolean flags for classification
    outage_related = models.BooleanField(default=False)
    is_planned_maintenance = models.BooleanField(default=False)
    is_root_cause_analysis = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification: {self.subject} ({self.timestamp.date()})"