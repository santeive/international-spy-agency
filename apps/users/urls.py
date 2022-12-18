"""
Users app url
"""

# Django
from django.urls import path
from .views import AuthViewSet, HitmenViewSet, ManagerViewSet

# Rest framework
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

USERS_ROUTER = SimpleRouter()

USERS_ROUTER.register(r'auth', AuthViewSet)
USERS_ROUTER.register(r'hitmen', HitmenViewSet)
USERS_ROUTER.register(r'manager', ManagerViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
