from django.db import models

from .service_request import ServiceRequest
from .service_request_bid import ServiceRequestBid

from accounts.models.profiles.business import BusinessProfile
from accounts.models.profiles.admin import AdminProfile


class ServiceContract(models.Model):

    service_request = models.ForeignKey(ServiceRequest,
                                        on_delete=models.CASCADE,
                                        related_name='service_contracts')
    experts = models.ManyToManyField(AdminProfile,
                                     related_name='contracts')
    server = models.ForeignKey(BusinessProfile,
                               on_delete=models.CASCADE,
                               related_name='service_contracts')
    days = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    bid = models.OneToOneField(ServiceRequestBid,
                               on_delete=models.CASCADE,
                               related_name='service_contract')
    canceled = models.BooleanField(default=False)
