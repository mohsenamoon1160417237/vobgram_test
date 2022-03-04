from django.db import models
from accounts.models.profiles.business import BusinessProfile
from .valid_skill import ValidSkill


class BusinessSkill(models.Model):

    business_profile = models.ForeignKey(BusinessProfile,
                                         on_delete=models.CASCADE,
                                         related_name='business_skills')
    valid_skill = models.ForeignKey(ValidSkill,
                                    on_delete=models.CASCADE,
                                    related_name='business_skills')
    score = models.PositiveIntegerField(default=0)

    class Meta:

        unique_together = [('valid_skill', 'business_profile')]
