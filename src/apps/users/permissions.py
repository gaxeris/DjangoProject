from rest_framework import permissions


class UserCustomPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ["retrieve", "update", "partial_update", "destroy"]:
            return obj.author == request.user or request.user.is_staff
        else:
            return False
