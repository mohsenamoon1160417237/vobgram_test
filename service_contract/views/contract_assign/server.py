from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from system_notification.utils.create_systemNotification import create_systemNotif

from service_contract.models.contract_assign import ContractAssign


class ServerAssignContract(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def post(self, request, ctr_asgn_id):

        contract_assign = get_object_or_404(ContractAssign, id=ctr_asgn_id)

        cnt = ContentType.objects.get_for_model(contract_assign)

        contract_assign.server_assigned = True
        contract_assign.save()

        rec = contract_assign.contract.service_request.requester
        first_name = request.user.personal_profile.first_name
        last_name = request.user.personal_profile.last_name

        create_systemNotif(rec,
                           '"{} {}" has assigned the contract'.format(first_name, last_name),
                           cnt,
                           ctr_asgn_id,
                           None)

        return Response({'status': 'server assigned contract'})
