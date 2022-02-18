from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep

from business_service.model_serializers.view.service_request_bid import ServiceRequestBidViewSerializer

from business_service.models.service_request import ServiceRequest
from business_service.models.service_request_bid import ServiceRequestBid


class ServiceRequestBidList(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request, serv_id):

        service_request = get_object_or_404(ServiceRequest, id=serv_id)

        bids = ServiceRequestBid.objects.filter(service_request=service_request)

        serializer = ServiceRequestBidViewSerializer(bids, many=True)

        return Response({'status': 'get service request bids list',
                         'service_request_bids': serializer.data})
