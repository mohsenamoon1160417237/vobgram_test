from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType

from admin_action.permissions.is_admin import IsAdmin

from business_skill.model_serializers.valid_skill import ValidSkillSerializer

from business_skill.models.valid_skill import ValidSkill
from accounts.models.system_data_confirm import SystemDataConfirm


class AdminNotconfirmedValidSkillList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):

        cnt = ContentType.objects.get(app_label='business_skill',
                                      model='validskill')

        confs = SystemDataConfirm.objects.filter(target_ct=cnt,
                                                 is_latest=True,
                                                 admin_profile__isnull=True)

        skills = ValidSkill.objects.filter(id__in=confs.values('target_id'))

        serializer = ValidSkillSerializer(skills, many=True)

        return Response({'status': 'get unconfirmed valid skills',
                         'skills': serializer.data})
