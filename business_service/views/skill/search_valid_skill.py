from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from accounts.permissions.profile_first_step import ProfileFirstStep
from business_service.models.valid_skill import ValidSkill
from business_service.model_serializers.valid_skill import ValidSkillSerializer



class SearchValidSkill(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]


    def get(self, request, query):

        skills = ValidSkill.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        skills = skills.filter(admin_data_confirm__is_confirmed=True)
        status = 'found skills'
        if skills.count() == 0:
            status = 'no skills found'

        serializer = ValidSkillSerializer(skills, many=True)
        data = {
            'skills': serializer.data,
            'status': status
        }

        return Response(data)
