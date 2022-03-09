from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from admin_action.permissions.is_admin_or_sup_vs import IsAdminOrSupVisor

from service_contract.models.contract_assign import ContractAssign

from service_contract.model_serializers.view.contract_assign import ContractAssignViewSerializer


class ContractAssignList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdminOrSupVisor]

    def get(self, request):

        user_type = request.user.user_type

        if user_type == 'admin':

            assigns = ContractAssign.objects.all()

        else:

            skills = request.user.sup_vs_profile.skill.all()
            assigns = ContractAssign.objects.filter(contract__skill__id__in=skills.values('id'))

        serializer = ContractAssignViewSerializer(assigns, many=True)

        return Response({'status': 'get contract assigns',
                         'assigns': serializer.data})
