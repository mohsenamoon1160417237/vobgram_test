from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType

from admin_action.permissions.is_admin import IsAdmin

from business_service.model_serializers.view.business_specialty import BusinessSpecialtyViewSerializer

from accounts.models.admin_data_confirm import AdminDataConfirm
from business_service.models.business_specialty import BusinessSpecialty



class AdminNotConfirmedBusinessSpecialtyList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):

        cnt = ContentType.objects.get_for_model(BusinessSpecialty)
        admin_confs = AdminDataConfirm.objects.filter(target_ct=cnt,
                                                      is_confirmed=False,
                                                      is_latest=True)

        specialties = BusinessSpecialty.objects.filter(id__in=admin_confs.values('target_id'))

        serializer = BusinessSpecialtyViewSerializer(specialties, many=True)

        return Response({'status': 'get unconfirmed specialties list',
                         'specialties': serializer.data})
