from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername
from accounts.permissions.obj.has_business_profile import ObjHasBusinessProfile

from accounts.models.UserRegistration import UserRegistration

from service_contract.models.contract_assign import ContractAssign
from service_contract.models.service_contract import ServiceContract

from service_contract.model_serializers.service_contract import ServiceContractSerializer
from business_service.model_serializers.service_request import ServiceRequestSerializer


class CustomerDirectContract(GenericAPIView):

    permission_classes = [IsAuthenticated,
                          ProfileFirstStep,
                          HasUsername,
                          ObjHasBusinessProfile]

    def get(self, request, ctr_id):

        contract = get_object_or_404(ServiceContract, id=ctr_id)

        serializer = ServiceContractSerializer(contract)

        return Response({'status': 'get contract',
                         'contract': serializer.data})

    def post(self, request, user_id):

        user = get_object_or_404(UserRegistration, id=user_id)
        self.check_object_permissions(request, user)

        customer_profile = request.user.customer_profile
        serv_req_data = request.data
        serv_req_data['requester_id'] = customer_profile.id
        serv_req_data['request_type'] = 'private'
        serv_req_data['max_days'] = request.data['days']

        req_serializer = ServiceRequestSerializer(data=serv_req_data)
        req_serializer.is_valid(raise_exception=True)
        service_request = req_serializer.save()

        ctr_data = request.data
        ctr_data['service_request_id'] = service_request.id
        ctr_data['customer_id'] = customer_profile.id
        ctr_data['server_id'] = user.business_profile.id
        serializer = ServiceContractSerializer(data=ctr_data)

        serializer.is_valid(raise_exception=True)

        contract = serializer.save()

        ContractAssign.objects.create(contract=contract)

        return Response({'status': 'created a direct contract',
                         'contract': serializer.data})
