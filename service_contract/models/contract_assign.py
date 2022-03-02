from django.db import models

from .service_contract import ServiceContract


class ContractAssign(models.Model):

    contract = models.OneToOneField(ServiceContract,
                                    on_delete=models.CASCADE,
                                    related_name='contract_assign')
    server_assigned = models.BooleanField(default=False)
    customer_assigned = models.BooleanField(default=False)
