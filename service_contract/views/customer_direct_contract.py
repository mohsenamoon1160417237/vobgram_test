from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername

from service_contract.models.contract_assign import ContractAssign
from service_contract.model_serializers.service_contract import ServiceContractSerializer


class CustomerDirectContract(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasUsername]

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
