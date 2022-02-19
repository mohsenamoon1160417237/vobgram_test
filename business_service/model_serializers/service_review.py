from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from business_service.models.service_review import ServiceReview
from business_service.models.service_request import ServiceRequest
from business_service.models.service_contract import ServiceContract

from .utils.update_business_profile_rate import update_business_profile_rate


class ServiceReviewSerializer(serializers.ModelSerializer):

    service_request_id = serializers.IntegerField()
    service_contract_id = serializers.IntegerField()

    class Meta:

        model = ServiceReview
        fields = ['service_request_id',
                  'service_contract_id',
                  'service_rating',
                  'service_note']

    def create(self, validated_data):

        service_request = get_object_or_404(ServiceRequest, id=validated_data['service_request_id'])
        service_contract = get_object_or_404(ServiceContract, id=validated_data['service_contract_id'])

        try:
            review = ServiceReview.objects.create(service_request=service_request,
                                                  service_contract=service_contract,
                                                  service_rating=validated_data['service_rating'],
                                                  service_note=validated_data['service_note'])

            server = service_contract.server

            update_business_profile_rate(server, validated_data['service_rating'])

            return review

        except IntegrityError:

            raise serializers.ValidationError({'error': 'You have added a review for this service already'})
