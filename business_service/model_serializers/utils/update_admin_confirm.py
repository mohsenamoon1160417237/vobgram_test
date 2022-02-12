from accounts.models.admin_data_confirm import AdminDataConfirm

from django.shortcuts import get_object_or_404


def update_admin_confirm(business_prof_obj, data_type, data_value):

    admin_confirm = get_object_or_404(AdminDataConfirm,
                                      business_profile=business_prof_obj,
                                      data_type=data_type)

    admin_confirm.data_value = data_value
    admin_confirm.save()
