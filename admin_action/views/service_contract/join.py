from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from admin_action.permissions.is_admin import IsAdmin

from service_contract.models.service_contract import ServiceContract


class ExpertJoinContract(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, cont_id):

        contract = get_object_or_404(ServiceContract, id=cont_id)

        contract.experts.add(request.user.expert_profile)
        contract.save()

        return Response({'status': 'joint contract'})
