from rest_framework import serializers

from business_service.models.business_product_vote import BusinessProductVote

from accounts.model_serializers.view.personal_profile import PersonalProfileViewSerializer


class BusinessProductVoteViewSerializer(serializers.ModelSerializer):

    voter = serializers.SerializerMethodField()

    class Meta:

        model = BusinessProductVote
        fields = ['voter',
                  'business_product',
                  'comment',
                  'date_time',
                  'id']

    def get_voter(self, obj):

        voter = obj.voter
        serializer = PersonalProfileViewSerializer(instance=voter)
        return serializer.data
