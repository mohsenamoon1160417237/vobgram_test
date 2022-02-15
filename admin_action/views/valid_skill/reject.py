from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import datetime

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from admin_action.permissions.is_admin import IsAdmin

from business_service.models.valid_skill import ValidSkill
from business_service.models.business_skill import BusinessSkill
from business_service.models.business_product import BusinessProduct

from accounts.models.admin_data_confirm import AdminDataConfirm


class AdminRejectValidSKill(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, skill_id):

        valid_skill = get_object_or_404(ValidSkill, id=skill_id)

        business_skills = BusinessSkill.objects.filter(valid_skill=valid_skill)

        cnt = ContentType.objects.get_for_model(valid_skill)
        admin_confirm = get_object_or_404(AdminDataConfirm,
                                          target_ct=cnt,
                                          target_id=valid_skill.id)
        admin_confirm.delete()

        for skill in business_skills:

            products = BusinessProduct.objects.filter(business_skill=skill)

            for product in products:

                product.business_skill = None
                product.save()

            skill.delete()

        valid_skill.delete()

        return Response({'status': 'rejected skill'})
