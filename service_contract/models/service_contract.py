from django.db import models

from business_service.models.service_request import ServiceRequest
from business_service.models.service_request_bid import ServiceRequestBid

from accounts.models.profiles.business import BusinessProfile
from accounts.models.profiles.sup_vs import SupVsProfile
from accounts.models.profiles.customer import CustomerProfile


class ServiceContract(models.Model):

    service_request = models.ForeignKey(ServiceRequest,
                                        on_delete=models.CASCADE,
                                        related_name='service_contracts',
                                        null=True)
    customer = models.ForeignKey(CustomerProfile,
                                 on_delete=models.CASCADE,
                                 related_name='service_contracts')
    sup_visor = models.ManyToManyField(SupVsProfile,
                                       related_name='contracts')
    title = models.CharField(max_length=200,
                             null=True,
                             blank=True)
    note = models.TextField(null=True,
                            blank=True)
    server = models.ForeignKey(BusinessProfile,
                               on_delete=models.CASCADE,
                               related_name='service_contracts')
    days = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    bid = models.OneToOneField(ServiceRequestBid,
                               on_delete=models.CASCADE,
                               related_name='service_contract',
                               null=True)
    canceled = models.BooleanField(default=False)
