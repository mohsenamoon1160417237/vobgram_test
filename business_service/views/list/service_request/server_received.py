from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from business_service.model_serializers.view.service_request.server import ServerReceivedServiceRequestViewSerializer


class ServerReceivedServiceRequestList(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request):

        user = request.user
        business_profile = user.business_profile

        serializer = ServerReceivedServiceRequestViewSerializer(business_profile)

        return Response({'status': 'get server service requests list',
                         'profile': serializer.data})
