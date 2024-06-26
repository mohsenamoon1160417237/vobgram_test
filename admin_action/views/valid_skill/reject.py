from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from admin_action.permissions.is_admin import IsAdmin
from system_notification.utils.sys_notif_manager import SystemNotificationManager

from business_skill.models.valid_skill import ValidSkill
from business_skill.models.business_skill import BusinessSkill
from business_service.models.business_product import BusinessProduct

from accounts.models.system_data_confirm import SystemDataConfirm
from system_notification.models.system_notification import SystemNotification


class AdminRejectValidSKill(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, skill_id):

        valid_skill = get_object_or_404(ValidSkill, id=skill_id)

        business_skills = BusinessSkill.objects.filter(valid_skill=valid_skill)

        cnt = ContentType.objects.get_for_model(valid_skill)
        admin_confirm = get_object_or_404(SystemDataConfirm,
                                          target_ct=cnt,
                                          target_id=valid_skill.id)

        user = admin_confirm.user

        admin_confirm.delete()

        for skill in business_skills:

            products = BusinessProduct.objects.filter(business_skill=skill)

            for product in products:

                product.business_skill = None
                product.save()

            skill.delete()

        notification = get_object_or_404(SystemNotification,
                                         target_ct=cnt,
                                         target_id=skill_id)

        notification.target_id = None
        notification.save()

        msg = 'Skill "{}" has been rejected by admin'.format(valid_skill.title)

        notif_mng = SystemNotificationManager(user, msg)
        notif_mng.doCreate()

        valid_skill.delete()

        return Response({'status': 'rejected skill'})
