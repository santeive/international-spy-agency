"""
Test for model users
"""
from django.test import TestCase
from apps.users.factories import UserFactory
from apps.users.models import User, Hitmen

class UserModelTest(TestCase):
    """
    User model test
    """
    @classmethod
    def setUpTestData(cls):
        UserFactory()
        cls.user = User.objects.first()

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

