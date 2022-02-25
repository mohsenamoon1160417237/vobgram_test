from django.db import models

from accounts.models.UserRegistration import UserRegistration
from business_service.models.valid_skill import ValidSkill


class AdminProfile(models.Model):

    user = models.OneToOneField(UserRegistration,
                                on_delete=models.CASCADE,
                                related_name='admin_profile')
    skills = models.ManyToManyField(ValidSkill,
                                    related_name='admin_profiles')
    confirmed_data_number = models.PositiveIntegerField(default=0)
