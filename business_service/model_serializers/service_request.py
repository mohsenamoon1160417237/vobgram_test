from rest_framework import serializers
from django.shortcuts import get_object_or_404

from business_service.models.service_request import ServiceRequest

from accounts.models.profiles.personal import PersonalProfile
from accounts.models.system_data_confirm import SystemDataConfirm


class ServiceRequestSerializer(serializers.ModelSerializer):

    requester_id = serializers.IntegerField()

    class Meta:

        model = ServiceRequest

        fields = ['requester_id',
                  'service_type',
                  'request_type',
                  'title',
                  'note',
                  'min_price',
                  'max_price',
                  'max_days']

    def create(self, validated_data):

        requester = get_object_or_404(PersonalProfile, id=validated_data['requester_id'])

        service_request = ServiceRequest.objects.create(requester=requester,
                                                        service_type=validated_data['service_type'],
                                                        request_type=validated_data['request_type'],
                                                        title=validated_data['title'],
                                                        note=validated_data['note'],
                                                        min_price=validated_data['min_price'],
                                                        max_price=validated_data['max_price'],
                                                        max_days=validated_data['max_days'])

        SystemDataConfirm.objects.create(target=service_request)

        return service_request

    def update(self, instance, validated_data):

        instance.service_type = validated_data['service_type']
        instance.title = validated_data['title']
        instance.note = validated_data['note']
        instance.min_price = validated_data['min_price']
        instance.max_price = validated_data['max_price']
        instance.max_days = validated_data['max_days']

        instance.save()

        return instance
