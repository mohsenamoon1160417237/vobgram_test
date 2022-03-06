from django.db import models

from accounts.models.UserRegistration import UserRegistration


class CustomerProfile(models.Model):

    user = models.OneToOneField(UserRegistration,
                                on_delete=models.CASCADE,
                                related_name='customer_profile')
