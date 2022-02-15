from rest_framework.permissions import BasePermission



class IsAdmin(BasePermission):

    message = 'You are not admin'

    def has_permission(self, request, view):

        user = request.user
        return user.user_type == 'admin'
