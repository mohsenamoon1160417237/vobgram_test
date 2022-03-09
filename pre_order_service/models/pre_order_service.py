from django.db import models

from accounts.models.profiles.business import BusinessProfile
from accounts.models.UserRegistration import UserRegistration


class PreOrderService(models.Model):

    owner = models.ForeignKey(BusinessProfile,
                              on_delete=models.CASCADE,
                              related_name='pre_order_services')
    title = models.CharField(max_length=200)
    description = models.TextField()
    registered_count = models.IntegerField(default=0)
    user_register = models.ManyToManyField(UserRegistration,
                                           related_name='pre_order_services')
    total_price = models.DecimalField(max_digits=8,
                                      decimal_places=2)
    off_amount = models.DecimalField(max_digits=8,
                                     decimal_places=2,
                                     default=0)
    off_price = models.DecimalField(max_digits=8,
                                    decimal_places=2,
                                    null=True)
