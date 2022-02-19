


def update_business_profile_rate(business_profile, new_rate):

    service_number = business_profile.service_number
    service_rate = business_profile.service_rate

    total_rate = service_rate * service_number

    total_rate += new_rate

    service_number += 1

    rate = total_rate / service_number

    business_profile.service_rate = rate
    business_profile.service_number = service_number

    business_profile.save()
