from django.shortcuts import get_object_or_404
import datetime

from accounts.models.admin_data_confirm import AdminDataConfirm


def admin_accept_or_reject(bool_type, data_type, admin_profile, target_ct, target_id, comment):

    admin_confirm = get_object_or_404(AdminDataConfirm,
                                      target_ct=target_ct,
                                      target_id=target_id,
                                      data_type=data_type)

    admin_confirm.is_confirmed = bool_type
    admin_confirm.admin_profile = admin_profile
    admin_confirm.date_time = datetime.datetime.now()
    admin_confirm.comment = comment
    admin_confirm.save()
