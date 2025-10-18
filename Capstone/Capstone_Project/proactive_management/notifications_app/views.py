from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mass_mail
from django.utils import timezone
from .serializers import CustomerSerializer, NotificationSerializer, EngineerSerializer
from .models import Customer, Notification, Engineer


# --- CustomerViewSet ---
class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Customer instances.
    Requires authentication.
    """
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


# --- NotificationViewSet ---
class NotificationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Notification instances, 
    including the custom 'send' action.
    """
    
    # We filter the queryset to ensure only 'draft' or 'ready' notifications can be modified
    def get_queryset(self):
        # Allow filtering by status, e.g., /api/notifications/?status=SENT
        queryset = Notification.objects.all().order_by('-timestamp')
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter.upper())
        return queryset

    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    
    # CRITICAL ADDITION: Custom action for sending emails
    # Maps to POST /api/notifications/{pk}/send/
    @action(detail=True, methods=['post'])
    def send(self, request, pk=None):
        """
        Takes a Notification ID, sends the email to all associated customers, 
        and updates the notification status.
        """
        try:
            notification = self.get_object() # Fetches the specific notification by primary key (pk)
        except Notification.DoesNotExist:
            return Response({'detail': 'Notification not found.'}, status=status.HTTP_404_NOT_FOUND)

        # 1. Check if the notification is ready to send
        if notification.status == 'SENT':
            return Response({'detail': 'This notification has already been sent.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 2. Prepare the email data
        recipient_emails = list(notification.customers.values_list('email', flat=True))

        if not recipient_emails:
             return Response({'detail': 'No customers selected for this notification.'}, status=status.HTTP_400_BAD_REQUEST)

        # The send_mass_mail function requires a tuple of tuples:
        # (subject, message, from_email, recipient_list)
        email_data = (
            (notification.subject, 
             notification.message_body, 
             'notifications@proactive.com', # Replace with your actual sender email
             recipient_emails),
        )

        # 3. Send the email (using the console backend in settings.py for development)
        try:
            # send_mass_mail returns the number of successfully sent messages
            messages_sent = send_mass_mail(email_data, fail_silently=False)
            
            # 4. Update the notification status upon success
            notification.status = 'SENT'
            notification.sent_at = timezone.now()
            # Ensure is_sent is updated for legacy compatibility if you kept it
            # notification.is_sent = True 
            notification.save()
            
            return Response({
                'detail': 'Notification sent successfully.',
                'messages_sent': messages_sent
            }, status=status.HTTP_200_OK)

        except Exception as e:
            # Handle potential email sending errors (e.g., SMTP failure)
            return Response({
                'detail': 'Failed to send notification.',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# --- EngineerViewSet ---
class EngineerViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing Engineer instances.
    """
    queryset = Engineer.objects.all().order_by('username')
    serializer_class = EngineerSerializer
    
    # Restrict permissions: Only authenticated users can view, but only superusers 
    # should be able to create/delete other engineers.
    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            # Example: Only allow superusers to create or delete engineers
            self.permission_classes = [IsAuthenticated] # You might use IsAdminUser for production
        elif self.action == 'retrieve':
             # Only allow engineers to see their own profile or list others
             self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated]
        
        return [permission() for permission in self.permission_classes]