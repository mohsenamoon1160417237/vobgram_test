from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType

from admin_action.permissions.is_admin import IsAdmin

from business_skill.model_serializers.business_specialty import BusinessSpecialtySerializer

from accounts.models.system_data_confirm import SystemDataConfirm
from business_skill.models.business_specialty import BusinessSpecialty


class AdminNotConfirmedBusinessSpecialtyList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):

        cnt = ContentType.objects.get(app_label='business_skill',
                                      model='businessspecialty')

        admin_confs = SystemDataConfirm.objects.filter(target_ct=cnt,
                                                       admin_profile__isnull=True,
                                                       is_latest=True)

        specialties = BusinessSpecialty.objects.filter(id__in=admin_confs.values('target_id'))

        serializer = BusinessSpecialtySerializer(specialties, many=True)

        return Response({'status': 'get unconfirmed specialties list',
                         'specialties': serializer.data})
