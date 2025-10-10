# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Adds a bio, profile picture, and a followers/following relationship.
    """
    bio = models.TextField(blank=True, default='', help_text="A short biography of the user.")
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='following'
    )

    def __str__(self):
        return self.username