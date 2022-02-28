from accounts.models.system_data_confirm import SystemDataConfirm

from django.contrib.contenttypes.models import ContentType



def create_admin_data_confirm(obj, business_profile, data_type):

    return SystemDataConfirm.objects.create(target=obj,
                                            business_profile=business_profile,
                                            data_type=data_type)
