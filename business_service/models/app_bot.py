from django.db import models

from accounts.models.profiles.business import BusinessProfile

from service_contract.models.service_contract import ServiceContract


class AppBot(models.Model):

    name = models.CharField(max_length=255)
    business_profile = models.ForeignKey(BusinessProfile,
                                         on_delete=models.SET_NULL,
                                         related_name='app_bot',
                                         null=True,
                                         blank=True)
    service_contract = models.ForeignKey(ServiceContract,
                                         on_delete=models.SET_NULL,
                                         related_name='app_bot',
                                         null=True,
                                         blank=True)
    dev_domain = models.CharField(max_length=255)

    class Meta:

        unique_together = [('business_profile', 'name'),
                           ('service_contract', 'name')]
