from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from admin_action.permissions.is_admin import IsAdmin

from admin_action.views.utils.admin_accept_or_reject import admin_accept_or_reject
from business_service.models.business_product import BusinessProduct


class AdminRejectBusinessProduct(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, prod_id):

        admin_profile = request.user.admin_profile

        product_step = get_object_or_404(BusinessProduct, id=prod_id)

        cnt = ContentType.objects.get_for_model(product_step)

        admin_accept_or_reject(False, None, admin_profile, cnt, prod_id, request.data['comment'])

        return Response({'status': 'rejected product'})
