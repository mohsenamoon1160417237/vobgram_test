from django.db import models

from .service_contract import ServiceContract
from accounts.models.admin_data_confirm import AdminDataConfirm


class ContractAssign(models.Model):

    contract = models.OneToOneField(ServiceContract,
                                    on_delete=models.CASCADE,
                                    related_name='contract_assign')
    admin_conf = models.OneToOneField(AdminDataConfirm,
                                      on_delete=models.CASCADE,
                                      related_name='contract_assign',
                                      null=True)
    server_assigned = models.BooleanField(default=False)
    customer_assigned = models.BooleanField(default=False)
