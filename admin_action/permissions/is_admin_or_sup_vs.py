from rest_framework.permissions import BasePermission


class IsAdminOrSupVisor(BasePermission):

    message = 'You are not a super visor or admin user'

    def has_permission(self, request, view):

        user_type = request.user.user_type

        return user_type == 'admin' or user_type == 'super_visor'
