from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername

from business_service.models.service_request import ServiceRequest
from service_contract.models.service_contract import ServiceContract

from business_service.model_serializers.service_review import ServiceReviewSerializer



class AddServiceReview(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasUsername]

    def post(self, request, serv_id):

        service_request = get_object_or_404(ServiceRequest, id=serv_id)

        service_contract = get_object_or_404(ServiceContract, service_request=service_request)

        serializer_data = {'service_request_id': serv_id,
                           'service_contract_id': service_contract.id,
                           'service_rating': request.data['service_rating'],
                           'service_note': request.data['service_note']}

        serializer = ServiceReviewSerializer(data=serializer_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'added service review',
                         'service_review': serializer.data})
