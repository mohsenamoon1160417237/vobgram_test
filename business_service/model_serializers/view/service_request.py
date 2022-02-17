from rest_framework import serializers

from business_service.models.service_request import ServiceRequest



class ServiceRequestViewSerializer(serializers.ModelSerializer):

    class Meta:

        model = ServiceRequest
        fields = ['service_type',
                  'title',
                  'note',
                  'least_budget',
                  'max_budget',
                  'finished',
                  'id']
