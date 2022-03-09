from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername

from service_contract.models.contract_assign import ContractAssign
from service_contract.models.service_contract import ServiceContract
from service_contract.model_serializers.service_contract import ServiceContractSerializer


class CustomerDirectContract(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasUsername]

    def get(self, request, ctr_id):

        contract = get_object_or_404(ServiceContract, id=ctr_id)

        serializer = ServiceContractSerializer(contract)

        return Response({'status': 'get contract',
                         'contract': serializer.data})

    def post(self, request, server_id):

        data = request.data
        data['customer_id'] = request.user.customer_profile.id
        data['server_id'] = server_id
        serializer = ServiceContractSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        contract = serializer.save()

        ContractAssign.objects.create(contract=contract)

        return Response({'status': 'created a direct contract',
                         'contract': serializer.data})
