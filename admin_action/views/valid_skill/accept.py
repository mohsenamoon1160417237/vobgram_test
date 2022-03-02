from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from admin_action.views.utils.admin_accept_or_reject import admin_accept_or_reject
from system_notification.utils.create_systemNotification import create_systemNotif

from admin_action.permissions.is_admin import IsAdmin

from business_service.models.valid_skill import ValidSkill
from accounts.models.system_data_confirm import SystemDataConfirm


class AdminAcceptValidSkill(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, skill_id):

        admin_profile = request.user.admin_profile

        skill = get_object_or_404(ValidSkill, id=skill_id)
        cnt = ContentType.objects.get_for_model(skill)

        admin_accept_or_reject(True, None, admin_profile, cnt, skill_id, None)

        sys_conf = get_object_or_404(SystemDataConfirm,
                                     target_ct=cnt,
                                     target_id=skill_id)

        business_profile = sys_conf.business_profile

        create_systemNotif(business_profile.user,
                           'Skill "{}" has been confirmed by admin'.format(skill.title),
                           skill,
                           None)

        return Response({'status': 'accepted skill'})
