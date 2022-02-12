from django.db import models

from .business_product import BusinessProduct
from accounts.models.admin_data_confirm import AdminDataConfirm


class BusinessProductStep(models.Model):

    business_product = models.ForeignKey(BusinessProduct,
                                         on_delete=models.CASCADE,
                                         related_name='product_steps')
    admin_data_confirm = models.OneToOneField(AdminDataConfirm,
                                              on_delete=models.DO_NOTHING,
                                              related_name='product_step')
    note = models.TextField(null=True,
                            blank=True)
    step_url = models.URLField()
    from_date = models.DateField()
    to_date = models.DateField()
    step_number = models.PositiveIntegerField()
