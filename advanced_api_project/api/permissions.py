from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow admin users to modify
        return request.user and request.user.is_staff
