from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType

from admin_action.permissions.is_admin import IsAdmin

from accounts.models.system_data_confirm import SystemDataConfirm
from pre_order_service.models.pre_order_service import PreOrderService
from pre_order_service.model_serializers.pre_order_service import PreOrderServiceSerializer


class NotConfirmedAdminPreOrderServiceList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):

        cnt = ContentType.objects.get(app_label='pre_order_service',
                                      model='preorderservice')

        confs = SystemDataConfirm.objects.filter(target_ct=cnt,
                                                 is_latest=True,
                                                 admin_profile__isnull=True)

        services = PreOrderService.objects.filter(id__in=confs.values('target_id'))

        serializer = PreOrderServiceSerializer(services, many=True)

        return Response({'status': 'get unconfirmed pre order services',
                         'services': serializer.data})
