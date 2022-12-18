from rest_framework.permissions import BasePermission, SAFE_METHODS

class HitsPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_superuser or request.user.is_manager
        
        if view.action in ['list', 'retrieve']:
            return True

        return False
