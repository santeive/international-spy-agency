"""
User app config
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    User app config class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
