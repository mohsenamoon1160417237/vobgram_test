from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep

from business_service.models.business_skill import BusinessSkill
from business_service.models.business_specialty import BusinessSpecialty

from accounts.models.admin_data_confirm import AdminDataConfirm
from accounts.models.profiles.business import BusinessProfile

from business_service.model_serializers.view.public.business_profile import PublicBusinessProfileViewSerializer


class SearchBusinessProfile(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request, query):

        skill_cnt = ContentType.objects.get(app_label='business_service',
                                            model='validskill')

        skill_admin_confs = AdminDataConfirm.objects.filter(target_ct=skill_cnt,
                                                            is_latest=True,
                                                            is_confirmed=True)

        skills = BusinessSkill.objects.filter(Q(valid_skill__title__icontains=query) |
                                              Q(valid_skill__description__icontains=query),
                                              score__gt=0,
                                              id__in=skill_admin_confs.values('target_id'))

        spec_cnt = ContentType.objects.get(app_label='business_service',
                                           model='businessspecialty')

        spec_admin_confs = AdminDataConfirm.objects.filter(target_ct=spec_cnt,
                                                           is_latest=True,
                                                           is_confirmed=True)

        specialties = BusinessSpecialty.objects.filter(id__in=spec_admin_confs.values('target_id'))

        prof_cnt = ContentType.objects.get(app_label='accounts',
                                           model='businessprofile')

        prof_admin_confs = AdminDataConfirm.objects.filter(target_ct=prof_cnt,
                                                           is_latest=True)

        for ad_conf in prof_admin_confs:

            if ad_conf.is_confirmed is False and ad_conf.admin_profile is not None:
                prof_admin_confs = prof_admin_confs.exclude(target_id=ad_conf.target_id)

        business_profiles = BusinessProfile.objects.filter(Q(id__in=skills.values('business_profile_id')) |
                                                           Q(id__in=specialties.values('business_profile_id')),
                                                           id__in=prof_admin_confs.values('target_id'))

        business_profiles = business_profiles.order_by('service_number', 'service_rate')

        if business_profiles.count() == 0:
            return Response({'status': 'no profiles'})

        serializer = PublicBusinessProfileViewSerializer(business_profiles, many=True)

        return Response({'status': 'profiles',
                         'profiles': serializer.data})
