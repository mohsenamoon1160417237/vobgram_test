from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from admin_action.permissions.is_admin import IsAdmin
from accounts.model_serializers.view.admin.business_profile import AdminBusinessProfileViewSerializer

from accounts.models.system_data_confirm import SystemDataConfirm
from accounts.models.profiles.business import BusinessProfile


class AdminNotConfirmedBusinessDataList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):

        profiles = BusinessProfile.objects.all()

        cnt = ContentType.objects.get(app_label='accounts',
                                      model='businessprofile')

        admin_confirms = SystemDataConfirm.objects.filter(target_ct=cnt)

        for profile in profiles:

            cnt = ContentType.objects.get_for_model(profile)

            cmp_name_conf = get_object_or_404(SystemDataConfirm,
                                              target_ct=cnt,
                                              target_id=profile.id,
                                              is_latest=True,
                                              data_type='company_name')

            cmp_phn_conf = cmp_name_conf = get_object_or_404(SystemDataConfirm,
                                                             target_ct=cnt,
                                                             target_id=profile.id,
                                                             is_latest=True,
                                                             data_type='company_phone_number')

            data_conf_checked = cmp_name_conf.admin_profile is not None and cmp_phn_conf.admin_profile is not None

            if data_conf_checked:

                profiles = profiles.exclude(id=profile.id)

                admin_confirms = admin_confirms.exclude(target_ct=cnt,
                                                        target_id=profile.id)

        profiles_serializer = AdminBusinessProfileViewSerializer(profiles, many=True)

        return Response({'status': 'get unconfirmed business profiles',
                         'profiles': profiles_serializer.data})
