from django.db import models

from accounts.models.profiles.business import BusinessProfile
from business_service.models.service_request import ServiceRequest


class ServiceRequestBid(models.Model):

    bidder = models.ForeignKey(BusinessProfile,
                               on_delete=models.CASCADE,
                               related_name='service_request_bids')
    service_request = models.ForeignKey(ServiceRequest,
                                        on_delete=models.CASCADE,
                                        related_name='service_request_bids')
    suggestion_text = models.CharField(max_length=200)
    price = models.IntegerField()
    days = models.IntegerField()

    class Meta:

        unique_together = [('bidder', 'service_request')]
