from rest_framework import serializers

from business_service.models.service_request import ServiceRequest


class CustomerServiceRequestViewSerializer(serializers.ModelSerializer):

    class Meta:

        model = ServiceRequest
        fields = ['service_type',
                  'title',
                  'note',
                  'least_budget',
                  'max_budget',
                  'max_days',
                  'finished',
                  'id']