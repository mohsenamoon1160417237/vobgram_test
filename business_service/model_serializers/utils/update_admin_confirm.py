from accounts.models.system_data_confirm import SystemDataConfirm

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType


def update_admin_confirm(business_prof_obj, data_type, data_value):

    cnt = ContentType.objects.get_for_model(business_prof_obj)

    admin_confirm = get_object_or_404(SystemDataConfirm,
                                      target_ct=cnt,
                                      target_id=business_prof_obj.id,
                                      data_type=data_type)

    admin_confirm.data_value = data_value
    admin_confirm.save()
