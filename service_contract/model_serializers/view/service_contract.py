from rest_framework import serializers

from service_contract.models.service_contract import ServiceContract
from business_service.model_serializers.view.service_request.customer import CustomerServiceRequestViewSerializer
from business_service.model_serializers.view.public.business_profile import PublicBusinessProfileViewSerializer

from accounts.model_serializers.view.admin_profile import AdminProfileViewSerializer


class ServiceContractViewSerializer(serializers.ModelSerializer):

    service_request = serializers.SerializerMethodField()
    server = serializers.SerializerMethodField()
    experts = serializers.SerializerMethodField()

    class Meta:

        model = ServiceContract
        fields = ['service_request',
                  'server',
                  'days',
                  'price',
                  'experts',
                  'bid',
                  'canceled']

    def get_service_request(self, obj):

        service_request = obj.service_request
        serializer = CustomerServiceRequestViewSerializer(service_request)
        return serializer.data

    def get_server(self, obj):

        server = obj.server
        serializer = PublicBusinessProfileViewSerializer(server)
        return serializer.data

    def get_experts(self, obj):

        experts = obj.experts.all()
        serializer = AdminProfileViewSerializer(experts, many=True)
        return serializer.data
