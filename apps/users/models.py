"""
Base user model
"""
# Django
from django.db import models
from django.utils import timezone
from django .contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    """
    Extension for the base user
    """
    name = models.CharField(max_length=30, help_text="Name assigned for this user")
    email = models.EmailField(unique=True, help_text="Email account for this user")
    description = models.CharField(max_length=80, help_text="Brief description for this position")
    is_active = models.BooleanField(default=True, help_text="General status for the user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return f'Name : {self.name} and {self.description}'

class Boss(User):
    """
    Model for the Boss
    """
    def __str__(self) -> str:
        return super().__str__()

class Manager(User):
    """
    Model for the Manager
    """
    def __str__(self) -> str:
        return super().__str__()

class Hitmen(User):
    """
    Model for the general user (Hitmen)
    """
    STATUS_MISSION = (
        ('A', 'Assigned'),
        ('FA', 'Failed Assigned'),
        ('C', 'Completed'),
    )
    status_mission =  models.CharField(max_length=2, choices=STATUS_MISSION, help_text="Status of missson")
    assigned_manager = models.ForeignKey(Manager, on_delete=models.CASCADE, help_text="Manager assigned for this hitmen")

    def __str__(self) -> str:
        return super().__str__()
