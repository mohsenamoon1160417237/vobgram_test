from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from system_notification.utils.create_systemNotification import create_systemNotif

from accounts.models.system_data_confirm import SystemDataConfirm
from business_service.models.service_request_bid import ServiceRequestBid
from service_contract.models.contract_assign import ContractAssign
from service_contract.models.service_contract import ServiceContract


class CustomerAcceptBid(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def post(self, request, bid_id):

        bid = get_object_or_404(ServiceRequestBid, id=bid_id)

        service_request = bid.service_request

        service_request.finished = True
        service_request.save()

        business_profile = bid.bidder

        contract = ServiceContract.objects.create(service_request=service_request,
                                                  server=business_profile,
                                                  customer=request.user.customer_profile,
                                                  days=bid.days,
                                                  price=bid.price,
                                                  title=service_request.title,
                                                  note=service_request.note,
                                                  bid=bid)

        ContractAssign.objects.create(contract=contract)

        first_name = request.user.personal_profile.first_name
        last_name = request.user.personal_profile.last_name

        create_systemNotif(business_profile.user,
                           '"{} {}" has accepted your bid on "{}" service request'.format(first_name,
                                                                                          last_name,
                                                                                          contract.title),
                           bid,
                           None)

        return Response({'status': 'created service contract'})
