from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .service_request import ServiceRequest
from service_contract.models.service_contract import ServiceContract


class ServiceReview(models.Model):

    service_request = models.OneToOneField(ServiceRequest,
                                           on_delete=models.CASCADE,
                                           related_name='service_review')
    service_contract = models.OneToOneField(ServiceContract,
                                            on_delete=models.CASCADE,
                                            related_name='service_review')

    service_rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                             MaxValueValidator(5)])
    service_note = models.CharField(max_length=300)
