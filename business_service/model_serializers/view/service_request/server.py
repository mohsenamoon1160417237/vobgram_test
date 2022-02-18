from rest_framework import serializers

from business_service.models.service_request import ServiceRequest
from accounts.models.profiles.business import BusinessProfile

from .customer import CustomerServiceRequestViewSerializer


class ServerReceivedServiceRequestViewSerializer(serializers.ModelSerializer):

    service_requests = serializers.SerializerMethodField()
    service_request_ids_this_user_has_bid = serializers.SerializerMethodField()

    class Meta:

        model = BusinessProfile
        fields = ['service_requests',
                  'service_request_ids_this_user_has_bid',
                  'id']

    def get_service_requests(self, obj):

        requests = obj.service_requests.all()
        serializer = CustomerServiceRequestViewSerializer(requests, many=True)

        return serializer.data

    def get_service_request_ids_this_user_has_bid(self, obj):

        bids = obj.service_request_bids.all()
        requests = ServiceRequest.objects.filter(id__in=bids.values('service_request_id'))

        ids = requests.values('id')

        return ids
