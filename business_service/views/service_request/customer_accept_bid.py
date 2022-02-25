from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep

from accounts.models.admin_data_confirm import AdminDataConfirm
from business_service.models.service_request_bid import ServiceRequestBid
from business_service.models.service_contract import ServiceContract
from business_service.models.contract_assign import ContractAssign


class CustomerAcceptBid(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def post(self, request, bid_id):

        bid = get_object_or_404(ServiceRequestBid, id=bid_id)
        service_request = bid.service_request

        service_request.finished = True
        service_request.save()

        business_profile = request.user.business_profile

        contract = ServiceContract.objects.create(service_request=service_request,
                                                  server=business_profile,
                                                  days=bid.days,
                                                  price=bid.price,
                                                  bid=bid)

        contract_assign = ContractAssign.objects.create(contract=contract)

        admin_conf = AdminDataConfirm.objects.create(target=contract_assign,
                                                     business_profile=business_profile)

        contract_assign.admin_conf = admin_conf
        contract_assign.save()

        return Response({'status': 'created service contract'})
