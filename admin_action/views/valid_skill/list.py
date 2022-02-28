from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from admin_action.permissions.is_admin import IsAdmin

from business_service.model_serializers.view.admin.valid_skill import AdminValidSkillViewSerializer
from business_service.model_serializers.valid_skill import ValidSkillSerializer

from business_service.models.valid_skill import ValidSkill
from accounts.models.system_data_confirm import SystemDataConfirm


class AdminNotconfirmedValidSkillList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):

        skills = ValidSkill.objects.all()

        for skill in skills:

            cnt = ContentType.objects.get_for_model(skill)
            admin_confirm = get_object_or_404(SystemDataConfirm,
                                              target_ct=cnt,
                                              target_id=skill.id)

            if admin_confirm.is_confirmed is True or admin_confirm.admin_profile is not None:

                skills = skills.exclude(id=skill.id)

        serializer = ValidSkillSerializer(skills, many=True)

        return Response({'status': 'get unconfirmed valid skills',
                         'skills': serializer.data})
