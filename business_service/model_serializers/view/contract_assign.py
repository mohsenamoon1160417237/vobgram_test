from rest_framework import serializers

from business_service.models.contract_assign import ContractAssign

from .service_contract import ServiceContractViewSerializer


class ContractAssignViewSerializer(serializers.ModelSerializer):

    contract = serializers.SerializerMethodField()

    class Meta:

        model = ContractAssign
        fields = ['contract',
                  'server_assigned',
                  'customer_assigned',
                  'id']

    def get_contract(self, obj):

        contract = obj.contract
        serializer = ServiceContractViewSerializer(contract)
        return serializer.data
