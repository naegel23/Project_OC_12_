from rest_framework import permissions
from .models import Client


class Permissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
            # Write permissions are only allowed to the owner of the snippet.
        try:
            var = obj.sales_contact == request.user
            return var
        except:
            var = obj['sales_contact'] == request.user
            return var


class EventPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.support_contact == request.user
