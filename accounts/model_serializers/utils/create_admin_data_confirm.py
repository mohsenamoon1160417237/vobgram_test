from accounts.models.admin_data_confirm import AdminDataConfirm



def create_admin_data_confirm(business_prf_obj, data_type, data_value):

    return AdminDataConfirm.objects.create(business_profile=business_prf_obj,
                                           data_type=data_type,
                                           data_value=data_value)
