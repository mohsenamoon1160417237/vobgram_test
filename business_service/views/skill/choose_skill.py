from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from business_service.models.valid_skill import ValidSkill
from business_service.models.business_skill import BusinessSkill

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from business_service.model_serializers.business_skill import BusinessSkillSerializer
from business_service.model_serializers.view.business_profile.private import PrivateBusinessProfileViewSerializer




class ChooseBusinessSkill(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request):

        user = request.user
        business_profile = user.business_profile
        serializer = PrivateBusinessProfileViewSerializer(business_profile)
        return Response({'status': 'get business profile',
                         'business_profile': serializer.data})

    def post(self, request):

        business_profile = request.user.business_profile
        business_profile_id = business_profile.id
        valid_skill = get_object_or_404(ValidSkill,
                                        title=request.data['title'],
                                        admin_data_confirm__is_confirmed=True)

        data = {
            'valid_skill_id': valid_skill.id,
            'business_profile_id': business_profile_id
        }

        serializer = BusinessSkillSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'choosed skill',
                         'skill': serializer.data})

    def delete(self, request):

        business_profile = request.user.business_profile
        title = request.data['title']
        valid_skill = get_object_or_404(ValidSkill, title=title)
        business_skill = get_object_or_404(BusinessSkill,
                                           business_profile=business_profile,
                                           valid_skill=valid_skill)
        business_skill.delete()
        valid_skill.selected_number -= 1
        valid_skill.save()
        return Response({'status': 'removed skill'})
