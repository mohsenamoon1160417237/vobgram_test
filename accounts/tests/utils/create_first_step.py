from .create_user import create_user
from accounts.models.profiles.personal import PersonalProfile


def create_first_step():

    user = create_user()
    PersonalProfile.objects.create(first_name='first name',
                                   last_name='last name',
                                   user=user)
    return user
