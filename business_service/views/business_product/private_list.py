from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from business_service.model_serializers.view.private.business_product import PrivateBusinessProductViewSerializer




class PrivateUserBusinessProductList(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request):

        user = request.user
        business_profile = user.business_profile
        products = business_profile.business_products.all()

        serializer = PrivateBusinessProductViewSerializer(products, many=True)
        return Response({'status': 'get business products',
                         'products': serializer.data})
