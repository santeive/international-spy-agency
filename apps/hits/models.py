"""
Hit model class
"""
# Django
from django.db import models
from django.utils import timezone
from apps.users.models import Manager, Hitmen

class Hit(models.Model):
    """
    Class Model for hit
    """
    STATUS_MISSION = (
        ('A', 'Assigned'),
        ('FA', 'Failed Assigned'),
        ('C', 'Completed'),
    )

    # Se va a utilizar otro tipo de delete
    assignee = models.ForeignKey(Hitmen, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=50, 
        help_text="Brief description for the hit"
    )
    target_name = models.CharField(
        max_length=30, 
        help_text="Name of the target to be terminated"
    )
    status_mission =  models.CharField(
        max_length=2, 
        choices=STATUS_MISSION, 
        help_text="Status of missson"
    )