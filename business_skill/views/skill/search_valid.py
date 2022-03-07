from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.permissions.profile_first_step import ProfileFirstStep

from business_skill.model_serializers.valid_skill import ValidSkillSerializer

from business_skill.views.utils.search_skillByTag import searchSkillByTag


class SearchValidSkill(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request, query):

        skills = searchSkillByTag(query)

        status = 'found skills'
        if skills.count() == 0:
            status = 'no skills found'

        serializer = ValidSkillSerializer(skills, many=True)
        data = {
            'skills': serializer.data,
            'status': status
        }

        return Response(data)
