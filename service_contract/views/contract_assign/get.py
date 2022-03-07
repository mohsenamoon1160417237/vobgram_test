from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername

from service_contract.models.contract_assign import ContractAssign
from service_contract.model_serializers.view.contract_assign import ContractAssignViewSerializer


class GetContractAssign(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasUsername]

    def get(self, request, ctr_asgn_id):

        contract_assign = get_object_or_404(ContractAssign, id=ctr_asgn_id)
        serializer = ContractAssignViewSerializer(contract_assign)
        return Response({'status': 'get contract assign',
                         'contract assign': serializer.data})
