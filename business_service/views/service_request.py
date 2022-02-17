from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep

from business_service.model_serializers.service_request import ServiceRequestSerializer
from business_service.model_serializers.view.service_request import ServiceRequestViewSerializer
from business_service.models.service_request import ServiceRequest


class AddServiceRequest(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request, serv_id):

        service_request = get_object_or_404(ServiceRequest, id=serv_id)

        serializer = ServiceRequestViewSerializer(service_request)

        return Response({'status': 'get a service request object',
                         'service_request': serializer.data})

    def post(self, request):

        data = request.data
        requester_id = request.user.personal_profile.id

        serializer_data = {'requester_id': requester_id,
                           'service_type': data['service_type'],
                           'title': data['title'],
                           'note': data['note'],
                           'least_budget': data['least_budget'],
                           'max_budget': data['max_budget']}

        serializer = ServiceRequestSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'created service request',
                         'service_request': serializer.data})

    def put(self, request, serv_id):

        service_request = get_object_or_404(ServiceRequest, id=serv_id)

        data = request.data

        requester_id = request.user.personal_profile.id

        serializer_data = {'requester_id': requester_id,
                           'service_type': data['service_type'],
                           'title': data['title'],
                           'note': data['note'],
                           'least_budget': data['least_budget'],
                           'max_budget': data['max_budget']}

        serializer = ServiceRequestSerializer(service_request, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'updated service request',
                         'service_request': serializer.data})

    def delete(self, request, serv_id):

        service_request = get_object_or_404(ServiceRequest, id=serv_id)

        service_request.delete()

        return Response({'status': 'deleted service request object'})
