from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom Admin interface for CustomUser model.
    """
    # Define which fields are shown on the change list page
    list_display = ('username', 'email', 'is_staff', 'date_of_birth')

    # Define which fields are shown on the edit page
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                   'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define fields for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)



