"""
Test for model users
"""
import json
from django.test import TestCase
from apps.users.factories import UserFactory
from rest_framework.views import status
from django.urls import reverse
from unittest.mock import Mock, patch

VALID_NAME = 'hitten'
VALID_EMAIL = 'hitten@isa.com'
VALID_PASSWORD = 'admin123-3'

class UserModelTest(TestCase):
    """
    User model test
    """
    @classmethod
    def setUpTestData(cls):
        user = UserFactory(email='boss@email.com')
        cls.user = user

    def login_user(self, email='', password=''):
        """
        Login user to get auth token
        """
        url=reverse('token_obtain_pair')
        return self.client.post(
            url,
            data=json.dumps({
                'email': email,
                'password': password
            }),
            content_type='application/json'
        )

    def signup_user(self, data):
        """
        Create api user and return auth token
        """
        url = reverse('user-register')
        return self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json'
        )
    
    def signup_complete_api_user(self, **kwargs):
        """
        Create api user using all fields
        """
        data = {
            'name': VALID_NAME,
            'email': VALID_EMAIL,
            'password': VALID_PASSWORD
        }
        data.update(kwargs)
        return self.signup_user(data)

    def test_user_fields_exists(self):
        """
        Test user fields existence
        """
        self.assertIsNotNone(self.user.name)
        self.assertIsNotNone(self.user.email)
        self.assertIsNotNone(self.user.description)
        self.assertIsNotNone(self.user.is_active)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)

    @patch('requests.post')
    def test_signup_user_with_valid_data(self, mocked_post):
        """
        Test sign up user with valid data
        """
        mocked_post.return_value = Mock(status_code=200)
        response = self.signup_user({
            'name': "hit",
            'email': "hit@isa.com",
            'password': "admin123-3",
        })

        # Assert access and refresh
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        # Assert status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)