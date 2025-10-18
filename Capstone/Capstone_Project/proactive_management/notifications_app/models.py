from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings 

# Choices for data consistency
SERVICE_CHOICES = [
    ('FIBER', 'Fiber Optic'),
    ('CABLE', 'Cable Internet'),
    ('DSL', 'DSL'),
    ('FIXED', 'Fixed Wireless')
]

NOTIFICATION_STATUS_CHOICES = [
    ('DRAFT', 'Draft'),
    ('READY', 'Ready to Send'),
    ('SENT', 'Sent'),
    ('FAILED', 'Failed'),
]


class Engineer(AbstractUser):
    """Custom User Model for Engineers with custom related names."""
    
    # Custom related names for M2M fields to avoid clashes with default Django auth
    groups = models.ManyToManyField(
        Group,
        related_name='engineer_groups', 
        blank=True,
        help_text='The groups this engineer belongs to. An engineer will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='engineer_permissions', 
        blank=True,
        help_text='Specific permissions for this engineer.'
    )

    
    class Meta:
        verbose_name = 'Engineer'
        verbose_name_plural = 'Engineers'
        
    def __str__(self):
        return self.username


class Customer(models.Model):
    """
    Central database for customer details, used for targeted communication.
    """
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(unique=True) # Must be unique
    last_mile_site = models.CharField(
        max_length=255, 
        help_text="e.g., street address or specific site name"
    )
    service_type = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES, # Using choices for filtering consistency
        default='FIBER'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.service_type})"


class Notification(models.Model):
    """
    Stores communication events managed by engineers.
    """
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, 
        null=True,
        related_name='notifications_created',
        verbose_name='Creating Engineer'
    )
    
    subject = models.CharField(max_length=255)
    message_body = models.TextField()
    
    # Many-to-Many relationship for recipients
    customers = models.ManyToManyField(
        Customer,
        related_name='notifications_received', 
        blank=True
    )
    
    # Workflow fields
    status = models.CharField(
        max_length=50,
        choices=NOTIFICATION_STATUS_CHOICES,
        default='DRAFT',
        help_text='Current status of the notification message.'
    )
    timestamp = models.DateTimeField(auto_now_add=True) # Creation time
    sent_at = models.DateTimeField(null=True, blank=True) # Actual sending time
    
    # Classification fields
    outage_related = models.BooleanField(default=False)
    is_planned_maintenance = models.BooleanField(default=False)
    is_root_cause_analysis = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.status}] {self.subject} by {self.created_by.username if self.created_by else 'System'}"