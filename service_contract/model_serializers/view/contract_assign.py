from rest_framework import serializers

from service_contract.models.contract_assign import ContractAssign

from service_contract.model_serializers.service_contract import ServiceContractSerializer


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
        serializer = ServiceContractSerializer(contract)
        return serializer.data
