from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername

from business_skill.views.utils.search_skillByTag import searchSkillByTag

from business_skill.models.business_skill import BusinessSkill
from business_skill.models.business_specialty import BusinessSpecialty

from accounts.models.system_data_confirm import SystemDataConfirm
from accounts.models.profiles.business import BusinessProfile

from business_service.model_serializers.view.public.business_profile import PublicBusinessProfileViewSerializer


class SearchBusinessProfile(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasUsername]

    def get(self, request, query):

        valid_skills = searchSkillByTag(query)

        business_skills = BusinessSkill.objects.filter(valid_skill__id__in=valid_skills.values('id'))

        spec_cnt = ContentType.objects.get(app_label='business_skill',
                                           model='businessspecialty')

        spec_admin_confs = SystemDataConfirm.objects.filter(target_ct=spec_cnt,
                                                            is_latest=True,
                                                            is_confirmed=True)

        specialties = BusinessSpecialty.objects.filter(Q(title__icontains=query) |
                                                       Q(note__icontains=query),
                                                       id__in=spec_admin_confs.values('target_id'))

        business_profiles = BusinessProfile.objects.filter(Q(id__in=business_skills.values('business_profile_id')) |
                                                           Q(id__in=specialties.values('business_profile_id')))

        business_profiles = business_profiles.order_by('service_number', 'service_rate')

        if business_profiles.count() == 0:
            return Response({'status': 'no profiles'})

        serializer = PublicBusinessProfileViewSerializer(business_profiles, many=True)

        return Response({'status': 'profiles',
                         'profiles': serializer.data})
