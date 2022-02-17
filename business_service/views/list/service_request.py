from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.permissions.profile_first_step import ProfileFirstStep

from business_service.model_serializers.view.service_request import ServiceRequestViewSerializer
from business_service.models.service_request import ServiceRequest


class UserServiceRequestList(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request):

        service_requests = ServiceRequest.objects.filter(requester__id=request.user.personal_profile.id)

        serializer = ServiceRequestViewSerializer(service_requests, many=True)

        return Response({'status': 'get service requests list',
                         'service_requests': serializer.data})
