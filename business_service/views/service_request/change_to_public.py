from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername

from accounts.models.system_data_confirm import SystemDataConfirm

from service_contract.models.service_contract import ServiceContract


class CustomerChangeRequestToPublic(GenericAPIView):

    permission_classes = [IsAuthenticated,
                          ProfileFirstStep,
                          HasUsername]

    def post(self, request, ctr_id):

        contract = get_object_or_404(ServiceContract, id=ctr_id)
        contract.canceled = True
        contract.save()

        service_request = contract.service_request
        service_request.finished = False
        service_request.request_type = 'public'
        service_request.min_price = request.data['min_price']
        service_request.max_price = request.data['max_price']
        service_request.max_days = request.data['max_days']

        service_request.save()

        cnt = ContentType.objects.get(app_label='business_service',
                                      model='servicerequest')

        confs = SystemDataConfirm.objects.filter(target_ct=cnt,
                                                 target_id=service_request.id,
                                                 is_latest=True)

        if not confs.exists():

            SystemDataConfirm.objects.create(target=service_request)

        return Response({'status': 'changed the request type to public'})
