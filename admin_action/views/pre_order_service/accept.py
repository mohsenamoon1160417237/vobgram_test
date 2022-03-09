from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from admin_action.permissions.is_admin import IsAdmin

from pre_order_service.models.pre_order_service import PreOrderService
from admin_action.views.utils.admin_accept_or_reject import admin_accept_or_reject


class AdminAcceptPreOrderService(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, ord_id):

        service = get_object_or_404(PreOrderService, id=ord_id)

        cnt = ContentType.objects.get_for_model(service)

        admin_accept_or_reject(True, None, request.user.admin_profile,
                               cnt, service.id, request.data['comment'])

        return Response({'status': 'accepted pre order service'})
