from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from accounts.permissions.profile_first_step import ProfileFirstStep
from business_service.models.business_skill import BusinessSkill
from accounts.models.profiles.business import BusinessProfile

from business_service.model_serializers.view.business_profile.public import PublicBusinessProfileViewSerializer




class SearchBusinessProfile(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request, query):

        skills = BusinessSkill.objects.filter(Q(valid_skill__title__icontains=query) |
                                              Q(valid_skill__description__icontains=query),
                                              valid_skill__admin_data_confirm__is_confirmed=True,
                                              score__gt=0)
        for skill in skills:

            business_profile = skill.business_profile
            admin_confirms = business_profile.admin_data_confirms.all()
            cmp_name_admin = admin_confirms.filter(data_type='company_name')[0]
            cmp_phn_admin = admin_confirms.filter(data_type='company_phone_number')[0]
            cmp_name_conf = cmp_name_admin.is_confirmed
            cmp_phn_conf = cmp_phn_admin.is_confirmed

            if cmp_name_conf is False or cmp_phn_conf is False:

                skills = skills.exclude(business_profile=business_profile)

        business_profiles = BusinessProfile.objects.filter(id__in=skills.values('business_profile_id'))
        business_profiles = business_profiles.order_by('service_number', 'service_rate')

        if business_profiles.count() == 0:
            return Response({'status': 'no profiles'})

        serializer = PublicBusinessProfileViewSerializer(business_profiles, many=True)

        return Response({'status': 'profiles',
                         'profiles': serializer.data})
