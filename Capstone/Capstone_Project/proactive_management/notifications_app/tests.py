# notifications_app/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core import mail 
from .models import Customer, Notification

Engineer = get_user_model()

class NotificationSendTest(APITestCase):
    def setUp(self):
        # 1. Create a test engineer
        self.engineer = Engineer.objects.create_user(
            username='test_engineer', 
            password='testpassword'
        )
        # 2. Log in and get a token
        login_url = reverse('api_token_auth') # Uses the 'api/login/' endpoint name
        response = self.client.post(login_url, {'username': 'test_engineer', 'password': 'testpassword'})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        
        # 3. Create test customers
        self.customer1 = Customer.objects.create(name='Cust A', email='a@example.com', location='NY', service_type='FIBER')
        self.customer2 = Customer.objects.create(name='Cust B', email='b@example.com', location='NY', service_type='CABLE')
        
        # 4. Create a draft notification
        self.draft_notification = Notification.objects.create(
            created_by=self.engineer,
            subject='Planned Maintenance Test',
            message_body='We are upgrading services tonight.',
            status='DRAFT'
        )
        self.draft_notification.customers.add(self.customer1, self.customer2)
        
        # URL for the custom send action
        self.send_url = reverse('notification-send', kwargs={'pk': self.draft_notification.pk})

    def test_can_send_notification(self):
        """Test that the notification is sent and status is updated."""
        
        # Initial check: no emails in the console
        self.assertEqual(len(mail.outbox), 0)
        
        # POST to the custom 'send' action
        response = self.client.post(self.send_url)
        
        # 1. Check API response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 2. Check that emails were sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Planned Maintenance Test')
        self.assertIn('a@example.com', mail.outbox[0].recipients)
        
        # 3. Check model update
        self.draft_notification.refresh_from_db()
        self.assertEqual(self.draft_notification.status, 'SENT')
        self.assertIsNotNone(self.draft_notification.sent_at)