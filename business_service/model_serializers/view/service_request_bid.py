from rest_framework import serializers

from business_service.models.service_request_bid import ServiceRequestBid
from accounts.models.profiles.business import BusinessProfile

from .public.business_profile import PublicBusinessProfileViewSerializer


class ServiceRequestBidViewSerializer(serializers.ModelSerializer):

    bidder = PublicBusinessProfileViewSerializer()

    class Meta:

        model = ServiceRequestBid
        fields = ['id',
                  'bidder',
                  'suggestion_text',
                  'price',
                  'days']
