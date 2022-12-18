"""
Factories for user models
"""
from .models import User, Hitmen
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for user model
    """

    class Meta:
        model = User

    name = "boss"
    email = "boss@isa.com"
    description = "This is an special hitmen"
    password = "admin123-3"
    is_active = True
    is_staff = True
    is_manager = False
    is_hitmen = False
    is_superuser = True