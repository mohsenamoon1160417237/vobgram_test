from django.db import models

from .pre_order_service import PreOrderService

class ServiceAttribute(models.Model):

    service = models.ForeignKey(PreOrderService,
                                on_delete=models.CASCADE,
                                related_name='service_attrs')
    title = models.CharField(max_length=150)
    note = models.CharField(max_length=300)
