from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername

from accounts.models.system_data_confirm import SystemDataConfirm

from business_service.models.service_request import ServiceRequest
from business_skill.models.valid_skill import ValidSkill


class CustomerAddSkillToServiceRequest(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasUsername]

    def post(self, request, req_id, skill_ttl):

        serv_request = get_object_or_404(ServiceRequest, id=req_id)

        cnt = ContentType.objects.get(app_label='business_skill', model='validskill')
        admin_confs = SystemDataConfirm.objects.filter(target_ct=cnt,
                                                       is_latest=True,
                                                       is_confirmed=True)

        skills = ValidSkill.objects.filter(title=skill_ttl,
                                           id__in=admin_confs.values('target_id'))

        if skills.exists():

            skill = skills[0]

            if not skill in serv_request.skill.all():

                serv_request.skill.add(skill)
                serv_request.save()

            return Response({'status': 'Added skill to service request'})

        else:

            raise ValidationError({'error': 'Skill not found'})
