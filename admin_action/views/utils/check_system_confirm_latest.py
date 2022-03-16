from accounts.models.system_data_confirm import SystemDataConfirm
from accounts.model_serializers.utils.create_admin_data_confirm import create_admin_data_confirm

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType


def check_system_confirm_latest(obj, user, data_type):

    cnt = ContentType.objects.get_for_model(obj)

    admin_confirm = get_object_or_404(SystemDataConfirm,
                                      target_ct=cnt,
                                      target_id=obj.id,
                                      data_type=data_type,
                                      is_latest=True)

    admin_profile = admin_confirm.admin_profile

    if admin_profile is not None:
        admin_confirm.is_latest = False
        admin_confirm.save()

        create_admin_data_confirm(obj, user, data_type)
