from rest_framework import permissions


class UserIsSelfPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return obj.username == request.user.username or request.user.is_staff
        else:
            return False
