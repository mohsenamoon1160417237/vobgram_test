from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.models.system_data_confirm import SystemDataConfirm

from business_skill.models.valid_skill import ValidSkill
from business_skill.model_serializers.valid_skill import ValidSkillSerializer


class SearchValidSkill(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request, query):

        cnt = ContentType.objects.get(app_label='business_service', model='validskill')

        admin_confs = SystemDataConfirm.objects.filter(target_ct=cnt,
                                                       is_latest=True,
                                                       is_confirmed=True)

        skills = ValidSkill.objects.filter(Q(title__icontains=query) |
                                           Q(description__icontains=query),
                                           id__in=admin_confs.values('target_id'))

        status = 'found skills'
        if skills.count() == 0:
            status = 'no skills found'

        serializer = ValidSkillSerializer(skills, many=True)
        data = {
            'skills': serializer.data,
            'status': status
        }

        return Response(data)
