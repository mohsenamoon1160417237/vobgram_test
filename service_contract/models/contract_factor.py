from django.db import models

from .service_contract import ServiceContract


class ContractFactor(models.Model):

    contract = models.ForeignKey(ServiceContract,
                                 on_delete=models.CASCADE,
                                 related_name='factors')
    amount = models.PositiveIntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    payment_service = models.CharField(max_length=100)
