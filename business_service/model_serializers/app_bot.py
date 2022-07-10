from rest_framework import serializers

from business_service.models.app_bot import AppBot
from accounts.models.profiles.business import BusinessProfile
from service_contract.models.service_contract import ServiceContract

from django.shortcuts import get_object_or_404
from django.db import IntegrityError


class AppBotSz(serializers.ModelSerializer):

    business_profile_id = serializers.IntegerField(allow_null=True)
    service_contract_id = serializers.IntegerField(allow_null=True)

    class Meta:

        model = AppBot
        fields = ['id',
                  'name',
                  'business_profile_id',
                  'service_contract_id',
                  'dev_domain']

        read_only_fields = ['id']

    def create(self, validated_data):

        bus_prof = get_object_or_404(BusinessProfile,
                                     id=validated_data['business_profile_id'])

        serv_cntr_id = validated_data['service_contract_id']

        if serv_cntr_id is not None:
            serv_cntr = get_object_or_404(ServiceContract,
                                          id=validated_data['service_contract_id'])
        else:
            serv_cntr = None

        try:
            app_bot = AppBot.objects.create(business_profile=bus_prof,
                                            service_contract=serv_cntr,
                                            name=validated_data['name'],
                                            dev_domain=validated_data['dev_domain'])

            return app_bot

        except IntegrityError:

            raise serializers.ValidationError({"error": "repeated bot name for service contract or business profile"})

    def update(self, instance, validated_data):

        instance.name = validated_data['name']

        serv_cntr_id = validated_data['service_contract_id']

        if serv_cntr_id is not None:
            serv_cntr = get_object_or_404(ServiceContract,
                                          id=validated_data['service_contract_id'])
            instance.service_contract = serv_cntr

        instance.dev_domain = validated_data['dev_domain']

        instance.save()
        return instance
