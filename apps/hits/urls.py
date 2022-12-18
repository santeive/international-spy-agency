"""
Hits app urls
"""

# Django
from django.urls import path
from .views import HitsViewSet

# Rest framework
from rest_framework.routers import SimpleRouter

HITS_ROUTER = SimpleRouter()
HITS_ROUTER.register(r'hits', HitsViewSet, basename='hits')