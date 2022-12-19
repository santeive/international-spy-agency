"""
User serializers
"""

from .models import Hitmen, User
from rest_framework import serializers, validators

class UserBaseSerializer(serializers.ModelSerializer):
    """
    Base serializer for User model
    """

    class Meta:
        model= User
        fields = ('id','name',)

class HitmenSignupSerializer(UserBaseSerializer):
    """
    Serializer for Hitmen creation
    """
    class Meta(UserBaseSerializer.Meta):
        fields = UserBaseSerializer.Meta.fields + ('email','password',)

class HitmenSerializer(serializers.ModelSerializer):
    """
    Serializer for Hitmen creation
    """
    assigned_manager = UserBaseSerializer(many=False, read_only=True)
    class Meta(serializers.ModelSerializer):
        model = Hitmen
        fields = (
            'id', 'name', 'email', 
            'description', 'is_hitmen', 
            'is_active', 'created_at', 
            'updated_at', 'assigned_manager'
        )