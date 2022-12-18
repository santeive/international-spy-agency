"""
User and ApiUser views
"""

from .models import Hitmen, User
from .serializers import HitmenSignupSerializer, HitmenSerializer
from .permissions import UserPermission, ManagerPermission

# Django
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

#restframework
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed, ValidationError, NotAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.mixins import (
    ListModelMixin, 
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin
)
from rest_framework.permissions import IsAuthenticated

class AuthViewSet(GenericViewSet):
    """
    API Endpoint that allows Users auth actions
    """
    queryset = User.objects.all()
    serializer_class = HitmenSignupSerializer

    @action(detail=False, methods=['post'])
    def register(self, request, *args, **kwargs):
        """
        Signup for hitmen users
        """
        try:
            serialized_hitmen = HitmenSignupSerializer(data=request.data)
            serialized_hitmen.is_valid(raise_exception=True)
        except ValidationError:
            raise ValidationError('Ya existe un usuario registrado con este email.')

        # Create hitmen with validated data, set password and save
        user = Hitmen.objects.create(**serialized_hitmen.validated_data)
        user.set_password(request.data['password'])
        user.is_hitmen = True
        user.save()

        # Get access and refresh token
        refresh = RefreshToken.for_user(user)
        token = {
            'message: ': 'Hitman Created',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        
        return Response(token, status=status.HTTP_201_CREATED)


class HitmenViewSet(GenericViewSet, ListModelMixin, 
    RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    """
    Viewset for Hitmen actions
    """
    permission_classes = [IsAuthenticated, UserPermission]
    queryset = Hitmen.objects.all()
    serializer_class = HitmenSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_manager:
            queryset = Hitmen.objects.filter(assigned_manager=user)
        else: #Boss
            queryset = super(HitmenViewSet, self).get_queryset()
        return queryset

    @action(detail=False, methods=['post'])
    def assign_manager(self, request, *args, **kwargs):
        """
        Custom action method for the boss to assign managers
        to hitmens.
        """
        hitmen_id = request.data['hitmen_id']
        manager_id = request.data['manager_id']
        
        hitmen = get_object_or_404(Hitmen, pk=hitmen_id)
        manager = User.objects.filter(is_manager=True, id=manager_id).first()
        if not hitmen.is_active:
            return Response(data={"message": "Can not assign to inactive users"}, status=status.HTTP_400_BAD_REQUEST)

        hitmen.assigned_manager = manager
        hitmen.save()

        return Response(data={"message": "Manager assigned"}, status=status.HTTP_200_OK)

class ManagerViewSet(GenericViewSet, ListModelMixin):
    """
    Viewset for Manager List operations for Boss
    """
    permission_classes = [IsAuthenticated, ManagerPermission]
    queryset = User.objects.filter(is_manager=True)
    serializer_class = HitmenSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = super(ManagerViewSet, self).get_queryset()
        return queryset

