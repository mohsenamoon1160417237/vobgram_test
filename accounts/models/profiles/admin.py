from django.db import models
from accounts.models.UserRegistration import UserRegistration


class AdminProfile(models.Model):

    user = models.OneToOneField(UserRegistration,
                                on_delete=models.CASCADE,
                                related_name='admin_profile')
    confirmed_data_number = models.PositiveIntegerField(default=0)
