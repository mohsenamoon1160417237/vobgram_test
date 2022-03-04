from rest_framework.permissions import BasePermission


class IsSupVisor(BasePermission):

    message = 'You are not a super visor user'

    def has_permission(self, request, view):

        user_type = request.user.user_type

        return user_type == 'super_visor'
