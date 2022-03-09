from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from admin_action.permissions.is_sup_vs import IsSupVisor
from system_notification.utils.create_systemNotification import create_systemNotif

from service_contract.models.service_contract import ServiceContract


class SupVisorJoinContract(GenericAPIView):

    permission_classes = [IsAuthenticated, IsSupVisor]

    def post(self, request, cont_id):

        contract = get_object_or_404(ServiceContract, id=cont_id)

        sup_vs_profile = request.user.sup_vs_profile

        if not sup_vs_profile in contract.sup_visor.all():

            contract.sup_visor.add(sup_vs_profile)
            contract.save()

            first_name = request.user.personal_profile.first_name
            last_name = request.user.personal_profile.last_name

            server = contract.server.user
            customer = contract.service_request.requester.user
            project_title = contract.service_request.title

            create_systemNotif(server,
                               '"{} {}" has joined to the project "{}"'.format(first_name,
                                                                               last_name,
                                                                               project_title),
                               contract,
                            None)

            create_systemNotif(customer,
                               '"{} {}" has joined to the project "{}"'.format(first_name,
                                                                               last_name,
                                                                               project_title),
                               contract,
                               None)

        return Response({'status': 'joint contract'})
