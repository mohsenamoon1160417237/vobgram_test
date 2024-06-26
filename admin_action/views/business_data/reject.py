from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from admin_action.permissions.is_admin import IsAdmin

from accounts.models.profiles.business import BusinessProfile

from admin_action.views.utils.admin_accept_or_reject import admin_accept_or_reject
from system_notification.utils.sys_notif_manager import SystemNotificationManager


class AdminRejectBusinessData(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, prof_id, data_type):

        admin_profile = request.user.admin_profile

        business_profile = get_object_or_404(BusinessProfile, id=prof_id)

        cnt = ContentType.objects.get_for_model(business_profile)

        admin_accept_or_reject(False, data_type, admin_profile, cnt, prof_id, request.data['comment'])

        if data_type == "company_phone_number":
            acc_field = business_profile.company_phone_number
        else:
            acc_field = business_profile.company_name

        msg = 'Your {} "{}" has been rejected by admin'.format(data_type,
                                                               acc_field)

        notif_mng = SystemNotificationManager(business_profile.user, msg)
        notif_mng.doCreate()

        return Response({'status': 'rejected business data'})
