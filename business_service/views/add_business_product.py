from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile
from accounts.models.admin_data_confirm import AdminDataConfirm

from business_service.models.business_product import BusinessProduct
from business_service.models.business_skill import BusinessSkill
from business_service.model_serializers.view.business_product import BusinessProductViewSerializer
from business_service.model_serializers.business_product import BusinessProductSerializer


class AddBusinessProduct(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request):

        user = request.user
        business_profile = user.business_profile
        products = business_profile.business_products

        serializer = BusinessProductViewSerializer(products, many=True)
        return Response({'status': 'get business products',
                         'products': serializer.data})

    def post(self, request):

        user = request.user
        business_profile = user.business_profile
        business_skill = get_object_or_404(BusinessSkill,
                                           business_profile=business_profile,
                                           valid_skill__title=request.data['skill_title'])

        serializer_data = {
            'business_skill_id': business_skill.id,
            'business_profile_id': business_profile.id,
            'title': request.data['title'],
            'description': request.data['description']
        }

        serializer = BusinessProductSerializer(data=serializer_data)
        status = 'created product'

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': status,
                         'product': serializer.data})

    def put(self, request, prod_id):

        product = get_object_or_404(BusinessProduct, id=prod_id)

        user = request.user
        business_profile = user.business_profile

        business_skill = get_object_or_404(BusinessSkill,
                                           business_profile=business_profile,
                                           valid_skill__title=request.data['skill_title'])
        serializer_data = {
            'business_skill_id': business_skill.id,
            'business_profile_id': business_profile.id,
            'title': request.data['title'],
            'description': request.data['description']
        }

        serializer = BusinessProductSerializer(product, data=serializer_data)
        status = 'updated product'

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': status,
                         'product': serializer.data})

    def delete(self, request, prod_id):

        product = get_object_or_404(BusinessProduct, id=prod_id)

        admin_confirm = get_object_or_404(AdminDataConfirm,
                                          business_profile=request.user.business_profile,
                                          data_type='business_product',
                                          data_value=product.title)

        product.delete()

        admin_confirm.delete()

        return Response({'status': 'deleted product'})
