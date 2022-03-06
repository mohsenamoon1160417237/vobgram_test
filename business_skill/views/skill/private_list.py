from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from business_skill.model_serializers.view.business_skill import BusinessSkillViewSerializer


class PrivateUserBusinessSkillList(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request):

        user = request.user
        business_profile = user.business_profile
        business_skills = business_profile.business_skills.all()
        serializer = BusinessSkillViewSerializer(business_skills, many=True)
        return Response({'status': 'get business skills',
                         'skills': serializer.data})
