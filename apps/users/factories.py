"""
Factories for user models
"""
from .models import User, Hitmen, Manager, Boss
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for user model
    """

    class Meta:
        model = User

    name = "Zero"
    email = "zero@isa.com"
    description = "This is an special hitmen"
    is_active = True