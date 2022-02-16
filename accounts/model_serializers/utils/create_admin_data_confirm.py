from accounts.models.admin_data_confirm import AdminDataConfirm

from django.contrib.contenttypes.models import ContentType



def create_admin_data_confirm(obj, data_type, data_value):

    return AdminDataConfirm.objects.create(target=obj,
                                           data_type=data_type,
                                           data_value=data_value)
