from django.db import models

from accounts.models.profiles.business import BusinessProfile
from accounts.models.profiles.personal import PersonalProfile


class ServiceRequest(models.Model):

    requester = models.ForeignKey(PersonalProfile,
                                  on_delete=models.CASCADE,
                                  related_name='service_requests')
    service_type = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    note = models.TextField()
    least_budget = models.PositiveIntegerField()
    max_budget = models.PositiveIntegerField()
    receivers = models.ManyToManyField(BusinessProfile,
                                       related_name='service_requests')
    finished = models.BooleanField(default=False)
