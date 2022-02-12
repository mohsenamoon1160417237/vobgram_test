from accounts.models.UserRegistration import UserRegistration


def create_user():

    user = UserRegistration.objects.create(phone_number="989366922661",
                                           registered=True,
                                           user_type="normal")
    user.set_password('mohsen12345678')
    user.save()
    return user
