from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from admin_action.permissions.is_admin import IsAdmin
from business_service.model_serializers.view.admin.business_product import AdminBusinessProductViewSerializer

from accounts.models.admin_data_confirm import AdminDataConfirm
from business_service.models.business_product import BusinessProduct


class AdminNotConfirmedBusinessProductList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):

        products = BusinessProduct.objects.all()

        for product in products:

            cnt = ContentType.objects.get_for_model(product)

            admin_confirm = get_object_or_404(AdminDataConfirm,
                                              target_ct=cnt,
                                              target_id=product.id)

            if admin_confirm.is_confirmed is True:

                product_steps = product.product_steps.all()

                all_confirmed = True

                for p_step in product_steps:

                    cnt = ContentType.objects.get_for_model(p_step)

                    admin_confirm = get_object_or_404(AdminDataConfirm,
                                                      target_ct=cnt,
                                                      target_id=p_step.id)

                    if admin_confirm.is_confirmed is False:

                        all_confirmed = False

                if all_confirmed is True:

                    products = products.exclude(id=product.id)

        serializer = AdminBusinessProductViewSerializer(products, many=True)

        return Response({'status': 'get unconfirmed products',
                         'products': serializer.data})
