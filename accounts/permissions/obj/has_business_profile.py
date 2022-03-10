from rest_framework.permissions import BasePermission

from accounts.models.profiles.business import BusinessProfile


class ObjHasBusinessProfile(BasePermission):

    message = "Server has not filled business profile"

    def has_object_permission(self, request, view, obj):

        business_profiles = BusinessProfile.objects.filter(user=obj)
        return business_profiles.exists()
