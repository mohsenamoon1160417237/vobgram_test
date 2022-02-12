from django.db import models
from accounts.models.profiles.business import BusinessProfile
from .profiles.admin import AdminProfile



class AdminDataConfirm(models.Model):

    admin_profile = models.ForeignKey(AdminProfile,
                                      on_delete=models.CASCADE,
                                      related_name='admin_data_confirms',
                                      null=True)
    business_profile = models.ForeignKey(BusinessProfile,
                                         on_delete=models.CASCADE,
                                         related_name='admin_data_confirms',
                                         null=True)
    data_type = models.CharField(max_length=30)
    data_value = models.CharField(max_length=30)
    is_confirmed = models.BooleanField(default=False)
    comment = models.TextField(null=True,
                               blank=True)
    date_time = models.DateTimeField(null=True)
    is_latest = models.BooleanField(default=True)
