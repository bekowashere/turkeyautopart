from rest_framework.permissions import BasePermission

class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
        
    message = "You are not superuser"
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser