from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from accounts.models.UserRegistration import UserRegistration


class SystemNotification(models.Model):

    receiver = models.ForeignKey(UserRegistration,
                                 on_delete=models.CASCADE,
                                 related_name='rec_notifs',
                                 null=True)
    sender = models.ForeignKey(UserRegistration,
                               on_delete=models.CASCADE,
                               related_name='sen_notifs',
                               null=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='rep_notif',
                               null=True)
    message = models.CharField(max_length=200)
    send_time = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    notif_type = models.CharField(max_length=200)
    target_ct = models.ForeignKey(ContentType,
                                  on_delete=models.CASCADE,
                                  related_name='notif_obj',
                                  null=True)
    target_id = models.PositiveIntegerField(null=True)
    target = GenericForeignKey('target_ct',
                               'target_id')
    url = models.URLField(null=True)
