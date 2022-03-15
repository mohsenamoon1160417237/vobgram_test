from django.db import models

from accounts.models.UserRegistration import UserRegistration


class SystemNotification(models.Model):

    receiver = models.ForeignKey(UserRegistration,
                                 on_delete=models.CASCADE,
                                 related_name='notifications')
    message = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
