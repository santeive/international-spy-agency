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
    DestroyModelMixin
)
# Integgrations
from apps.users.models import User, Hitmen
from .models import Hit
from .serializers import HitSerializer
from apps.users.serializers import UserBaseSerializer

class HitsViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Hit.objects.all()
    serializer_class = HitSerializer

    def get_queryset(self):
        queryset = super(HitsViewSet, self).get_queryset()
        return queryset

    def create(self, request, *args, **kwargs):
        """
        Create hit action
        """
        request_data = request.data
        assignee = Hitmen.objects.get(id=request_data['assignee'])

        request_data['assignee'] = assignee
        hit_serializer = self.get_serializer(data=request_data)
        hit_serializer.is_valid(raise_exception=True)

        hit = hit_serializer.save()
        return Response(self.serializer_class(hit).data, status=status.HTTP_201_CREATED)