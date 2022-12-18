"""
Test for Hit models
"""
from django.urls import reverse
from apps.users.models import User
from rest_framework.views import status
from django.test import TestCase
from ..factories import HitFactory

# Create your tests here.
class HitTestCase(TestCase):
    """
    Hit model test
    """
    def setUp(self):
        email = "hey@isa.com"
        password = "admin123-3"
        self.credentials = {
            'email': 'testuser',
            'password': 'secret'}
        self.user = User.objects.create_user(**self.credentials)

        jwt_fetch_data = {
            'email':email,
            'password':password
        }

        url = reverse('token_obtain_pair')
        response = self.client.post(url, jwt_fetch_data, format='json')
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.hit = HitFactory()

    
    def test_hit_listing(self):
        url = reverse('hits-list')
        response = self.client.get(url, data={'format': 'json'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hit_fields_exists(self):
        """
        Test hit fields existance
        """
        self.assertIsNotNone(self.hit.description)
        self.assertIsNotNone(self.hit.target_name)
        self.assertIsNotNone(self.hit.status_mission)
