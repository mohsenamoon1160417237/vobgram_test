from accounts.models.UserRegistration import UserRegistration
from accounts.models.profiles.admin import AdminProfile



def create_admin_user():

    user = UserRegistration.objects.create(phone_number='989366922661',
                                           user_type='admin',
                                           registered=True)

    user.set_password('mohsen1160417237')
    user.save()

    AdminProfile.objects.create(user=user)

    return user
