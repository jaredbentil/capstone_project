from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class Engineer(AbstractUser):
    """
    Custom user model for engineers with standard Django authentication features.
    """
    is_engineer = models.BooleanField(default=True)

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
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_sent = models.BooleanField(default=False)
    created_by = models.ForeignKey(Engineer, on_delete=models.SET_NULL, null=True, related_name='notifications_created')
    customers = models.ManyToManyField(Customer, related_name='notifications')
    sent_at = models.DateTimeField(null=True, blank=True)
    outage_related = models.BooleanField(default=False)

    def __str__(self):
        return self.titl
