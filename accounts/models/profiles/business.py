from django.db import models

from accounts.models.UserRegistration import UserRegistration


class BusinessProfile(models.Model):

    user = models.OneToOneField(UserRegistration,
                                on_delete=models.CASCADE,
                                related_name='business_profile')
    company_name = models.CharField(max_length=100)
    company_phone_number = models.CharField(max_length=14)
    bio = models.TextField(null=True,
                           blank=True)
    service_number = models.PositiveIntegerField(default=0)
    service_rate = models.FloatField(default=0)
