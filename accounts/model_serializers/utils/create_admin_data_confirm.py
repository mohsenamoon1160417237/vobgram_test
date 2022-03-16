from accounts.models.system_data_confirm import SystemDataConfirm


def create_admin_data_confirm(obj, user, data_type):

    return SystemDataConfirm.objects.create(target=obj,
                                            user=user,
                                            data_type=data_type)
