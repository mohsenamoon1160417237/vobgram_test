from django.db import models

from accounts.models.UserRegistration import UserRegistration

from business_service.models.valid_skill import ValidSkill


class ExpertProfile(models.Model):

    user = models.OneToOneField(UserRegistration,
                                on_delete=models.CASCADE,
                                related_name='expert_profile')
    skills = models.ManyToManyField(ValidSkill,
                                    related_name='expert_profiles')
