"""
Hits viewsets
"""
# rest framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin, 
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin
)
# Django
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Integgrations
from apps.users.models import User, Hitmen
from .permissions import HitsPermission
from .models import Hit
from .serializers import HitSerializer, HitCreateSerializer
from apps.users.serializers import UserBaseSerializer
from rest_framework.permissions import IsAuthenticated

class HitsViewSet(GenericViewSet, ListModelMixin, 
    RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    permission_classes = [IsAuthenticated, HitsPermission]
    queryset = Hit.objects.all()
    serializer_class = HitSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_manager:
            queryset = Hit.objects.filter(Q(assignment_creator=user) | Q(assignee=user))
        elif user.is_hitmen:
            queryset = Hit.objects.filter(assignee = user)
        else: # Boss
            queryset = super(HitsViewSet, self).get_queryset()
        
        return queryset

    def create(self, request, *args, **kwargs):
        """
        Create hit action
        """
        request_data = request.data
        assignment_creator = self.request.user

        try: 
            assignee = get_object_or_404(User, id=request_data['assignee'])

            request_data['assignee'] = assignee.pk
            request_data['assignment_creator'] = assignment_creator.pk

            hit_serializer = HitCreateSerializer(data=request_data)
            hit_serializer.is_valid(raise_exception=True)

            hit = hit_serializer.save()
        except:
            return Response(
                data={"message": "Error when assigning user"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(self.serializer_class(hit).data, status=status.HTTP_201_CREATED)