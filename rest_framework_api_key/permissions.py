from rest_framework import permissions
from rest_framework_api_key.models import APIKey


class HasAPIAccess(permissions.BasePermission):
    message = 'Invalid or missing API Key.'

    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_API_KEY', '')
        return APIKey.objects.filter(key=api_key).exists()

class HasAPIAccessOrIsAuthenticated(permissions.BasePermission):
    """Authorize if a valid API key is provided or request is authenticated."""

    def has_permission(self, request, view):
        perms = [
            HasAPIAccess(),
            permissions.IsAuthenticated(),
        ]
        return any(perm.has_permission(request, view) for perm in perms)
