from django.db import models

from accounts.models.UserRegistration import UserRegistration

from business_skill.models.valid_skill import ValidSkill


class SupVsProfile(models.Model):

    user = models.OneToOneField(UserRegistration,
                                on_delete=models.CASCADE,
                                related_name='sup_vs_profile')
    skill = models.ManyToManyField(ValidSkill,
                                   related_name='sup_vs_profiles')
