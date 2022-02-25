from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep

from business_service.models.contract_assign import ContractAssign
from business_service.model_serializers.view.contract_assign import ContractAssignViewSerializer


class GetContractAssign(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request, ctr_asgn_id):

        contract_assign = get_object_or_404(ContractAssign, id=ctr_asgn_id)
        serializer = ContractAssignViewSerializer(contract_assign)
        return Response({'status': 'get contract assign',
                         'contract assign': serializer.data})
