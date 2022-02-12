from rest_framework.permissions import BasePermission
from accounts.models.profiles.business import BusinessProfile


class HasBusinessProfile(BasePermission):

    message = 'You must add your business data'

    def has_permission(self, request, view):
        business_profiles = BusinessProfile.objects.filter(user=request.user)
        return business_profiles.exists()
