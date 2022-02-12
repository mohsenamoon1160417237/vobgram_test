from django.db import models

from accounts.models.profiles.personal import PersonalProfile
from .business_product import BusinessProduct


class BusinessProductVote(models.Model):

    voter = models.ForeignKey(PersonalProfile,
                              on_delete=models.CASCADE,
                              related_name='product_votes')
    business_product = models.ForeignKey(BusinessProduct,
                                         on_delete=models.CASCADE,
                                         related_name='product_votes')
    comment = models.CharField(max_length=299,
                               null=True,
                               blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    