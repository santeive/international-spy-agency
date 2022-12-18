"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.contrib import admin
from django.urls import path, include, re_path

# restframework
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAuthenticated

# Integrations
from apps.users.urls import USERS_ROUTER
from apps.hits.urls import HITS_ROUTER

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

V1_ROUTER = DefaultRouter()

V1_ROUTER.registry.extend(USERS_ROUTER.registry)
V1_ROUTER.registry.extend(HITS_ROUTER.registry)

schema_view = get_schema_view(
   openapi.Info(
      title="International Spy Agency",
      default_version='v1',
      description="This is the documentation for ISA project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.users.urls")),
    path('api/v1/', include(V1_ROUTER.urls)),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
