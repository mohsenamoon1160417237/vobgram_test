from rest_framework import serializers
from django.shortcuts import get_object_or_404

from business_service.models.business_product_vote import BusinessProductVote
from business_service.models.business_product import BusinessProduct
from business_service.models.business_product_vote import BusinessProductVote

from accounts.models.profiles.personal import PersonalProfile



class BusinessProductVoteSerializer(serializers.ModelSerializer):

    voter_id = serializers.IntegerField()
    business_product_id = serializers.IntegerField()

    class Meta:

        model = BusinessProductVote
        fields = ['voter_id',
                  'business_product_id',
                  'comment']

    def create(self, validated_data):

        voter = get_object_or_404(PersonalProfile, id=validated_data['voter_id'])
        product = get_object_or_404(BusinessProduct, id=validated_data['business_product_id'])
        vote = BusinessProductVote.objects.create(voter=voter,
                                                  business_product=product,
                                                  comment=validated_data['comment'])
        product.total_up_votes += 1
        product.save()

        return vote
