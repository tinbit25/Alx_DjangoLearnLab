from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """Custom permission to allow only admins to modify data."""
    
    def has_permission(self, request, view):
        # Read-only access for all
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only admin users can modify data
        return request.user and request.user.is_staff
