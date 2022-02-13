from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.db.models import Q

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.models.admin_data_confirm import AdminDataConfirm

from business_service.models.valid_skill import ValidSkill
from business_service.model_serializers.valid_skill import ValidSkillSerializer



class SearchValidSkill(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]


    def get(self, request, query):

        skills = ValidSkill.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        for skill in skills:
            cnt = ContentType.objects.get_for_model(skill)
            admin_confirm = get_object_or_404(AdminDataConfirm,
                                              target_ct=cnt,
                                              target_id=skill.id)

            if admin_confirm.is_confirmed is False:
                skills = skills.exclude(id=skill.id)

        status = 'found skills'
        if skills.count() == 0:
            status = 'no skills found'

        serializer = ValidSkillSerializer(skills, many=True)
        data = {
            'skills': serializer.data,
            'status': status
        }

        return Response(data)
