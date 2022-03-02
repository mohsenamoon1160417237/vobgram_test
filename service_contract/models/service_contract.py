from django.db import models

from business_service.models.service_request import ServiceRequest
from business_service.models.service_request_bid import ServiceRequestBid

from accounts.models.profiles.business import BusinessProfile
from accounts.models.profiles.expert import ExpertProfile


class ServiceContract(models.Model):

    service_request = models.ForeignKey(ServiceRequest,
                                        on_delete=models.CASCADE,
                                        related_name='service_contracts')
    experts = models.ManyToManyField(ExpertProfile,
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
