"""
Hit model class
"""
# Django
from django.db import models
from django.utils import timezone
from apps.users.models import Hitmen, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Hit(models.Model):
    """
    Class Model for hit
    """
    STATUS_MISSION = (
        ('A', 'Assigned'),
        ('FA', 'Failed Assigned'),
        ('C', 'Completed'),
    )

    #Hitmen/Manager
    assignee = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="assigee",
        help_text="Manager assigned for this hitmen"
    )

    """ assignee = models.ForeignKey(
        Hitmen,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    ) """
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
    assignment_creator = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="hitcreator"
    )