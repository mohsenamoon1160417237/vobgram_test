from accounts.models.profiles.business import BusinessProfile



def create_business_profile(user):

    business_profile = BusinessProfile.objects.create(user=user,
                                                      company_name='mohsen',
                                                      company_phone_number='123345')
    return business_profile
