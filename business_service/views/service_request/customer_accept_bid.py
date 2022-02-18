from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep

from business_service.models.service_request_bid import ServiceRequestBid
from business_service.models.service_contract import ServiceContract



class CustomerAcceptBid(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def post(self, request, bid_id):

        bid = get_object_or_404(ServiceRequestBid, id=bid_id)
        service_request = bid.service_request

        service_request.finished = True
        service_request.save()

        contract = ServiceContract.objects.create(service_request=service_request,
                                                  server=request.user.business_profile,
                                                  days=bid.days,
                                                  price=bid.price,
                                                  bid=bid)

        return Response({'status': 'created service contract'})
