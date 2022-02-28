from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile
from accounts.models.system_data_confirm import SystemDataConfirm

from business_service.models.business_product import BusinessProduct
from business_service.models.business_skill import BusinessSkill

from business_service.model_serializers.view.private.business_product import PrivateBusinessProductViewSerializer
from business_service.model_serializers.business_product import BusinessProductSerializer


class AddBusinessProduct(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request, prod_id):

        product = get_object_or_404(BusinessProduct, id=prod_id)
        serializer = PrivateBusinessProductViewSerializer(product)
        return Response({'status': 'get a product object',
                         'product': serializer.data})

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

        cnt = ContentType.objects.get_for_model(product)

        admin_confirm = get_object_or_404(SystemDataConfirm,
                                          target_ct=cnt,
                                          target_id=product.id)

        product.delete()

        admin_confirm.delete()

        return Response({'status': 'deleted product'})
