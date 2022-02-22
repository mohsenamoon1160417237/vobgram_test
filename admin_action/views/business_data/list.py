from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType

from admin_action.permissions.is_admin import IsAdmin
from accounts.model_serializers.view.admin.business_profile import AdminBusinessProfileViewSerializer

from accounts.models.admin_data_confirm import AdminDataConfirm
from accounts.models.profiles.business import BusinessProfile


class AdminNotConfirmedBusinessDataList(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):

        profiles = BusinessProfile.objects.all()

        sample_profile = profiles[0]

        cnt = ContentType.objects.get_for_model(sample_profile)

        admin_confirms = AdminDataConfirm.objects.filter(target_ct=cnt)

        for profile in profiles:

            cnt = ContentType.objects.get_for_model(profile)

            data_confs = AdminDataConfirm.objects.filter(target_ct=cnt,
                                                         target_id=profile.id)

            cmp_name_conf = data_confs.filter(data_type='company_name')[0]
            cmp_phn_conf = data_confs.filter(data_type='company_phone_number')[0]

            data_conf_true = cmp_phn_conf.is_confirmed is True and cmp_name_conf.is_confirmed is True
            data_conf_checked = cmp_name_conf.admin_profile is not None and cmp_phn_conf.admin_profile is not None

            if data_conf_true or data_conf_checked:

                profiles = profiles.exclude(id=profile.id)

                admin_confirms = admin_confirms.exclude(target_ct=cnt,
                                                        target_id=profile.id)

        profiles_serializer = AdminBusinessProfileViewSerializer(profiles, many=True)

        return Response({'status': 'get unconfirmed business profiles',
                         'profiles': profiles_serializer.data})
