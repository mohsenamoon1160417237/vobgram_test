from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from business_service.model_serializers.valid_skill import ValidSkillSerializer
from business_service.model_serializers.business_skill import BusinessSkillSerializer


class AddValidSkill(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def post(self, request):

        serializer = ValidSkillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        skill = serializer.save()

        business_profile = request.user.business_profile
        business_profile_id = business_profile.id

        data = {
            'valid_skill_id': skill.id,
            'business_profile_id': business_profile_id,
            'comment': ''
        }

        serializer = BusinessSkillSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'added new skill',
                         'skill': serializer.data})
