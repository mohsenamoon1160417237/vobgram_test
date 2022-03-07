from rest_framework.permissions import BasePermission


class HasUsername(BasePermission):

    message = 'First choose your username'

    def has_permission(self, request, view):

        profile = request.user.personal_profile

        return profile.username is not None
