"""
Permissions for users views
"""
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    """
    User views permissions
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if view.action == 'assign_manager':
            return request.user.is_superuser

        if view.action in ['list', 'retrieve', 'update', 'partial_update']:
            return True


        return False