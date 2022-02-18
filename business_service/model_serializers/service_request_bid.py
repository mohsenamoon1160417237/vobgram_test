from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from business_service.models.service_request_bid import ServiceRequestBid
from business_service.models.service_request import ServiceRequest

from accounts.models.profiles.business import BusinessProfile



class ServiceRequestBidSerializer(serializers.ModelSerializer):

    bidder_id = serializers.IntegerField()
    service_request_id = serializers.IntegerField()

    class Meta:

        model = ServiceRequestBid
        fields = ['bidder_id',
                  'service_request_id',
                  'suggestion_text',
                  'price',
                  'days']

    def validate(self, data):

        service_request = get_object_or_404(ServiceRequest,
                                            id=data['service_request_id'])

        least_budj = service_request.least_budget
        max_budj = service_request.max_budget

        price = data['price']

        if price < least_budj:

            raise serializers.ValidationError('price is too low')

        elif price > max_budj:

            raise serializers.ValidationError('price is too high')

        max_days = service_request.max_days

        if max_days is not None:

            days = data['days']

            if days > max_days:

                raise serializers.ValidationError('days are longer than the request max days')

        return data

    def create(self, validated_data):

        bidder = get_object_or_404(BusinessProfile,
                                   id=validated_data['bidder_id'])

        service_request = get_object_or_404(ServiceRequest,
                                            id=validated_data['service_request_id'])

        try:
            bid = ServiceRequestBid.objects.create(bidder=bidder,
                                                   service_request=service_request,
                                                   suggestion_text=validated_data['suggestion_text'],
                                                   price=validated_data['price'],
                                                   days=validated_data['days'])
            return bid

        except IntegrityError:

            raise serializers.ValidationError({'error': 'You have already bid on this request'})
