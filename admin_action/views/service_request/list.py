from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.contrib.contenttypes.models import ContentType

from rest_framework.permissions import IsAuthenticated
from admin_action.permissions.is_admin import IsAdmin

from accounts.models.admin_data_confirm import AdminDataConfirm

from business_service.models.contract_assign import ContractAssign
from business_service.models.service_request import ServiceRequest

from business_service.model_serializers.view.service_request.customer import CustomerServiceRequestViewSerializer


class AdminNotConfirmedServiceRequestList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):

        cnt = ContentType.objects.get(app_label='business_service',
                                      model='servicerequest')

        admin_confs = AdminDataConfirm.objects.filter(target_ct=cnt,
                                                      is_latest=True,
                                                      is_confirmed=False,
                                                      admin_profile__isnull=True)

        service_requests = ServiceRequest.objects.filter(id__in=admin_confs.values('target_id'))

        serializer = CustomerServiceRequestViewSerializer(service_requests, many=True)

        return Response({'status': 'get unconfirmed service requests',
                         'requests': serializer.data})
