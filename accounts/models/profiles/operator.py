from django.db import models

from accounts.models.UserRegistration import UserRegistration


class OperatorProfile(models.Model):

    user = models.OneToOneField(UserRegistration,
                                on_delete=models.CASCADE,
                                related_name='operator_profile')
    