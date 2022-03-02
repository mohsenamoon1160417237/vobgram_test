from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from accounts.models.UserRegistration import UserRegistration


class SystemNotification(models.Model):

    receiver = models.ForeignKey(UserRegistration,
                                 on_delete=models.CASCADE,
                                 related_name='notifications')
    message = models.CharField(max_length=200)
    target_ct = models.ForeignKey(ContentType,
                                  on_delete=models.CASCADE,
                                  related_name='obj')
    target_id = models.PositiveIntegerField(null=True)
    target = GenericForeignKey(target_ct, target_id)
    data_type = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
