from rest_framework import serializers
from django.shortcuts import get_object_or_404

from service_contract.models.service_contract import ServiceContract
from business_service.models.service_request import ServiceRequest
from accounts.models.profiles.customer import CustomerProfile
from accounts.models.profiles.business import BusinessProfile

from business_service.model_serializers.view.service_request.customer import CustomerServiceRequestViewSerializer
from business_service.model_serializers.view.public.business_profile import PublicBusinessProfileViewSerializer

from accounts.model_serializers.view.sup_visor import SupVisorProfileViewSerializer
from accounts.model_serializers.view.customer import CustomerProfileViewSerializer

from business_skill.model_serializers.valid_skill import ValidSkillSerializer

from system_notification.utils.sys_notif_manager import SystemNotificationManager


class ServiceContractSerializer(serializers.ModelSerializer):

    service_request = serializers.SerializerMethodField()
    server = serializers.SerializerMethodField()
    sup_visors = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()
    customer_id = serializers.IntegerField()
    server_id = serializers.IntegerField()
    service_request_id = serializers.IntegerField()

    class Meta:

        model = ServiceContract
        fields = ['service_request_id',
                  'service_request',
                  'server',
                  'days',
                  'price',
                  'sup_visors',
                  'bid',
                  'canceled',
                  'id',
                  'customer',
                  'customer_id',
                  'server_id']

        read_only_fields = ['service_request',
                            'server',
                            'bid',
                            'canceled',
                            'sup_visors',
                            'customer',
                            'skills',
                            'id']

        write_only_fields = ['customer_id',
                             'server_id']

    def get_service_request(self, obj):

        service_request = obj.service_request
        serializer = CustomerServiceRequestViewSerializer(service_request)
        return serializer.data

    def get_server(self, obj):

        server = obj.server
        serializer = PublicBusinessProfileViewSerializer(server)
        return serializer.data

    def get_sup_visors(self, obj):

        sup_visors = obj.sup_visor.all()
        serializer = SupVisorProfileViewSerializer(sup_visors, many=True)
        return serializer.data

    def get_customer(self, obj):

        customer = obj.customer
        serializer = CustomerProfileViewSerializer(customer)
        return serializer.data

    def get_skills(self, obj):

        skills = obj.skill.all()
        serializer = ValidSkillSerializer(skills, many=True)
        return serializer.data

    def create(self, validated_data):

        customer = get_object_or_404(CustomerProfile, id=validated_data['customer_id'])
        server = get_object_or_404(BusinessProfile, id=validated_data['server_id'])
        service_request = get_object_or_404(ServiceRequest,
                                            id=validated_data['service_request_id'])

        contract = ServiceContract.objects.create(service_request=service_request,
                                                  customer=customer,
                                                  server=server,
                                                  price=validated_data['price'],
                                                  days=validated_data['days'])

        first_name = customer.user.personal_profile.first_name
        last_name = customer.user.personal_profile.last_name

        msg = '"{} {}" has created a contract with you'.format(first_name, last_name)

        notif_mng = SystemNotificationManager(server.user, msg)
        notif_mng.doCreate()

        return contract
