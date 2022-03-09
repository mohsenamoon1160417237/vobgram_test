from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername

from pre_order_service.models.pre_order_service import PreOrderService


class CustomerUnRegisterPreOrderService(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasUsername]

    def post(self, request, ord_id):

        pre_order_service = get_object_or_404(PreOrderService, id=ord_id)

        if request.user in pre_order_service.user_register.all():

            pre_order_service.user_register.remove(request.user)
            pre_order_service.registered_count -= 1
            pre_order_service.save()

        return Response({'status': 'unregistered from pre order service'})
