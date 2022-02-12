from rest_framework.permissions import BasePermission
from accounts.models.profiles.personal import PersonalProfile



class ProfileFirstStep(BasePermission):

    message = 'You must complete your profile'

    def has_permission(self, request, view):

        user = request.user
        profiles = PersonalProfile.objects.filter(user__id=user.id)
        if not profiles.exists():
            return False
        profile = profiles[0]
        first_name = profile.first_name
        last_name = profile.last_name

        if (first_name is None) or (last_name is None):
            return False
        return True
