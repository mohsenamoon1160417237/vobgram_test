from rest_framework.permissions import BasePermission


class IsAdminOrExpert(BasePermission):

    message = 'You are not an expert or admin'

    def has_permission(self, request, view):

        user_type = request.user.user_type

        return user_type == 'admin' or user_type == 'expert'
