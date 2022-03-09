from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.models.system_data_confirm import SystemDataConfirm

from pre_order_service.models.pre_order_service import PreOrderService
from pre_order_service.model_serializers.pre_order_service import PreOrderServiceSerializer


class PreOrderServiceList(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request):

        cnt = ContentType.objects.get(app_label='pre_order_service',
                                      model='preorderservice')

        confs = SystemDataConfirm.objects.filter(target_ct=cnt,
                                                 is_latest=True,
                                                 is_confirmed=True)

        services = PreOrderService.objects.filter(id__in=confs.values('target_id'))

        serializer = PreOrderServiceSerializer(services, many=True)

        return Response({'status': 'get pre order services',
                         'services': serializer.data})
