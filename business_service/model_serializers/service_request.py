from rest_framework import serializers
from django.shortcuts import get_object_or_404

from business_service.models.service_request import ServiceRequest

from accounts.models.profiles.personal import PersonalProfile
from accounts.models.admin_data_confirm import AdminDataConfirm


class ServiceRequestSerializer(serializers.ModelSerializer):

    requester_id = serializers.IntegerField()

    class Meta:

        model = ServiceRequest

        fields = ['requester_id',
                  'service_type',
                  'title',
                  'note',
                  'least_budget',
                  'max_budget',
                  'max_days']

    def create(self, validated_data):

        requester = get_object_or_404(PersonalProfile, id=validated_data['requester_id'])

        service_request = ServiceRequest.objects.create(requester=requester,
                                                        service_type=validated_data['service_type'],
                                                        title=validated_data['title'],
                                                        note=validated_data['note'],
                                                        least_budget=validated_data['least_budget'],
                                                        max_budget=validated_data['max_budget'],
                                                        max_days=validated_data['max_days'])

        AdminDataConfirm.objects.create(target=service_request)

        return service_request

    def update(self, instance, validated_data):

        instance.service_type = validated_data['service_type']
        instance.title = validated_data['title']
        instance.note = validated_data['note']
        instance.least_budget = validated_data['least_budget']
        instance.max_budget = validated_data['max_budget']
        instance.max_days = validated_data['max_days']

        instance.save()

        return instance
