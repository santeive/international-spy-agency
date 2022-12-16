"""
User and ApiUser views
"""

from .models import Hitmen, Manager, Boss, User
from .serializers import HitmenSignupSerializer, UserBaseSerializer

#restframework
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed, ValidationError, NotAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class AuthViewSet(GenericViewSet):
    """
    API Endpoint that allows Users auth actions
    """
    queryset = User.objects.all()
    serializer_class = HitmenSignupSerializer

    @action(detail=False, methods=['post'])
    def signup(self, request, *args, **kwargs):
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
        user.save()

        # Get access and refresh token
        refresh = RefreshToken.for_user(user)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        
        return Response(token, status=status.HTTP_201_CREATED)

