# notifications_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Engineer, Customer, Notification

# Register Engineer using the custom UserAdmin
@admin.register(Engineer)
class CustomUserAdmin(UserAdmin):
    # Customize the fieldsets/list display if necessary
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    # Use the default UserAdmin, or customize further

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location', 'service_type', 'created_at')
    search_fields = ('name', 'email', 'location', 'last_mile_site')
    list_filter = ('service_type', 'location')
    ordering = ('name',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_by', 'status', 'sent_at', 'is_planned_maintenance', 'outage_related')
    search_fields = ('subject', 'message_body')
    list_filter = ('status', 'outage_related', 'is_planned_maintenance')
    # Display the many-to-many field correctly
    filter_horizontal = ('customers',) 
    readonly_fields = ('timestamp', 'sent_at')