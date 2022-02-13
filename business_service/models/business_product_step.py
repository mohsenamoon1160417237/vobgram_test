from django.db import models

from .business_product import BusinessProduct


class BusinessProductStep(models.Model):

    business_product = models.ForeignKey(BusinessProduct,
                                         on_delete=models.CASCADE,
                                         related_name='product_steps')
    note = models.TextField(null=True,
                            blank=True)
    step_url = models.URLField()
    from_date = models.DateField()
    to_date = models.DateField()
    step_number = models.PositiveIntegerField()
