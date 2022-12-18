"""
Serializers for hits app
"""
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from .models import Hit
from apps.users.serializers import UserBaseSerializer, HitmenSerializer

class HitSerializer(serializers.ModelSerializer):
    """
    Serializer class for it model
    """
    class Meta:
        model = Hit
        fields = ('id', 'assignee', 'description', 'target_name', 'status_mission','assignment_creator')
