from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from rest_framework.permissions import IsAuthenticated
from admin_action.permissions.is_admin import IsAdmin
from system_notification.utils.create_systemNotification import create_systemNotif

from service_contract.models.service_contract import ServiceContract


class ExpertLeaveContract(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, cont_id):

        contract = get_object_or_404(ServiceContract, id=cont_id)
        cnt = ContentType.objects.get_for_model(contract)

        contract.experts.remove(request.user.expert_profile)
        contract.save()

        first_name = request.user.personal_profile.first_name
        last_name = request.user.personal_profile.last_name

        server = contract.server
        customer = contract.service_request.requester
        project_title = contract.service_request.title

        create_systemNotif(server,
                           '"{} {}" has left the project "{}"'.format(first_name,
                                                                      last_name,
                                                                      project_title),
                           cnt,
                           cont_id,
                           None)

        create_systemNotif(customer,
                           '"{} {}" has left the project "{}"'.format(first_name,
                                                                      last_name,
                                                                      project_title),
                           cnt,
                           cont_id,
                           None)

        return Response({'status': 'left contract'})
