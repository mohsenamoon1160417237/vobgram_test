from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername

from system_notification.utils.sys_notif_manager import SystemNotificationManager

from service_contract.models.contract_assign import ContractAssign


class CustomerAssignContract(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasUsername]

    def post(self, request, ctr_asgn_id):

        contract_assign = get_object_or_404(ContractAssign, id=ctr_asgn_id)

        contract_assign.customer_assigned = True
        contract_assign.save()
        contract = contract_assign.contract
        service_request = contract.service_request

        rec = contract_assign.contract.server.user
        first_name = request.user.personal_profile.first_name
        last_name = request.user.personal_profile.last_name

        msg = '"{} {}" has assigned the contract "{}"'.format(first_name,
                                                              last_name,
                                                              service_request.title)

        notif_mng = SystemNotificationManager(rec, msg)
        notif_mng.doCreate()

        return Response({'status': 'customer assigned contract'})
