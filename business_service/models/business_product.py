from django.db import models

from accounts.models.profiles.business import BusinessProfile
from business_skill.models.business_skill import BusinessSkill


class BusinessProduct(models.Model):

    business_profile = models.ForeignKey(BusinessProfile,
                                         on_delete=models.CASCADE,
                                         related_name='business_products')
    business_skill = models.ForeignKey(BusinessSkill,
                                       on_delete=models.DO_NOTHING,
                                       related_name='business_products',
                                       null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    max_step_number = models.PositiveIntegerField(default=0)
    total_up_votes = models.PositiveIntegerField(default=0)

    class Meta:

        unique_together = [('title', 'business_profile')]
