from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.obj.has_business_profile import ObjHasBusinessProfile

from accounts.models.UserRegistration import UserRegistration

from business_service.model_serializers.view.public.business_profile import PublicBusinessProfileViewSerializer
from business_service.model_serializers.view.private.business_profile import PrivateBusinessProfileViewSerializer


class ViewProfile(GenericAPIView):

    permission_classes = [IsAuthenticated,
                          ProfileFirstStep,
                          ObjHasBusinessProfile]

    def get(self, request, id):

        user = get_object_or_404(UserRegistration, id=id)
        self.check_object_permissions(request, user)

        business_profile = user.business_profile

        if request.user == user:

            serializer = PrivateBusinessProfileViewSerializer(business_profile)
            status = 'private profile'

        else:

            serializer = PublicBusinessProfileViewSerializer(business_profile)
            status = 'public profile'

        return Response({'status': status,
                         'profile': serializer.data})
