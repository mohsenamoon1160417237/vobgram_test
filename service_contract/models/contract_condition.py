from django.db import models

from .service_contract import ServiceContract


class ContractCondition(models.Model):

    contract = models.ForeignKey(ServiceContract,
                                 on_delete=models.CASCADE,
                                 related_name='conditions')
    description = models.TextField()
