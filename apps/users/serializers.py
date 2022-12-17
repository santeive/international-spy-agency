"""
User serializers
"""

from .models import Hitmen, Manager, Boss, User
from rest_framework import serializers, validators

class UserBaseSerializer(serializers.ModelSerializer):
    """
    Base serializer for User model
    """

    class Meta:
        model= User
        fields = ('name', 'email', 'description')

class HitmenSignupSerializer(UserBaseSerializer):
    """
    Serializer for Hitmen creation
    """
    class Meta(UserBaseSerializer.Meta):
        fields = UserBaseSerializer.Meta.fields + ('password',)

class HitmenSerializer(UserBaseSerializer):
    """
    Serializer for Hitmen creation
    """
    class Meta(serializers.ModelSerializer):
        fields = ('id', 'name', 'email', 'description')