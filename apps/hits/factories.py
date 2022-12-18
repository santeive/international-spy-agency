import factory
from .models import Hit
from apps.users.factories import UserFactory

class HitFactory(factory.django.DjangoModelFactory):
    """
    Factory for Hit model
    """

    class Meta:
        model = Hit

    description = "Special Mission"
    target_name = "Kula Diamond"
    status_mission = "A"
    