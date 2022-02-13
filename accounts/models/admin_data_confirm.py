from django.db import models

from .profiles.admin import AdminProfile

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class AdminDataConfirm(models.Model):

    admin_profile = models.ForeignKey(AdminProfile,
                                      on_delete=models.CASCADE,
                                      related_name='admin_data_confirms',
                                      null=True)
    target_ct = models.ForeignKey(ContentType,
                                  on_delete=models.CASCADE,
                                  related_name='obj')
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_ct', 'target_id')
    data_type = models.CharField(max_length=30,
                                 null=True)
    data_value = models.CharField(max_length=50,
                                  null=True)
    is_confirmed = models.BooleanField(default=False)
    comment = models.TextField(null=True,
                               blank=True)
    date_time = models.DateTimeField(null=True)
    is_latest = models.BooleanField(default=True)
