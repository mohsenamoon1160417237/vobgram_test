from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.models.profiles.business import BusinessProfile

from business_service.model_serializers.view.business_profile.public import PublicBusinessProfileViewSerializer
from business_service.model_serializers.view.business_profile.private import PrivateBusinessProfileViewSerializer



class ViewProfile(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request, id):

        business_profile = get_object_or_404(BusinessProfile, id=id)
        user = request.user

        if user == business_profile.user:

            serializer = PrivateBusinessProfileViewSerializer(business_profile)
            status = 'private profile'

        else:

            serializer = PublicBusinessProfileViewSerializer(business_profile)
            status = 'public profile'

        return Response({'status': status,
                         'profile': serializer.data})
