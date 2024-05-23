from rest_framework import permissions


class BlogPostCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        if view.action == "get_recent_posts":
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action in ["retrieve", "update", "partial_update", "destroy"]:
            return obj.author == request.user or request.user.is_staff
        else:
            return False
