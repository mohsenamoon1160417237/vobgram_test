from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from business_service.models.business_product import BusinessProduct
from business_service.models.business_product_vote import BusinessProductVote

from business_service.model_serializers.business_product_vote import BusinessProductVoteSerializer
from business_service.model_serializers.view.business_product_vote import BusinessProductVoteViewSerializer


class AddBusinessProductVote(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep,  HasBusinessProfile]

    def get(self, request, vote_id):

        vote = get_object_or_404(BusinessProduct, id=vote_id)
        serializer = BusinessProductVoteViewSerializer(vote)
        return Response({'status': 'get product votes',
                         'votes': serializer.data})

    def post(self, request, prod_id):

        user = request.user
        voter_id = user.personal_profile.id

        serializer_data = {'voter_id': voter_id,
                           'business_product_id': prod_id,
                           'comment': request.data['comment']}

        serializer = BusinessProductVoteSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'up voted the product',
                         'vote': serializer.data})

    def delete(self, request, vote_id):

        vote = get_object_or_404(BusinessProductVote, id=vote_id)
        product = vote.business_product
        vote.delete()
        product.total_up_votes -= 1
        product.save()

        return Response({'status': 'removed upvote'})
