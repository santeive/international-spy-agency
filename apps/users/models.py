"""
Base user model
"""
# Django
from django.db import models
from django.utils import timezone
from django .contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager

# Manager
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """
    Extension for the base user
    """
    name = models.CharField(
        max_length=30, 
        help_text="Name assigned for this user"
    )
    email = models.EmailField(
        unique=True, 
        help_text="Email account for this user"
    )
    description = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        help_text="Brief description for this position"
    )
    is_staff = models.BooleanField(('staff_status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        default=True, 
        help_text="General status for the user"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

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
    assigned_manager = models.ForeignKey(
        Manager, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Manager assigned for this hitmen"
    )

    def __str__(self) -> str:
        return super().__str__()
