from django.db import models

from accounts.models.profiles.business import BusinessProfile
from accounts.models.profiles.personal import PersonalProfile

from business_skill.models.valid_skill import ValidSkill


class ServiceRequest(models.Model):

    requester = models.ForeignKey(PersonalProfile,
                                  on_delete=models.CASCADE,
                                  related_name='service_requests')
    request_type = models.CharField(max_length=100)
    service_type = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    note = models.TextField()
    min_price = models.PositiveIntegerField(null=True)
    max_price = models.PositiveIntegerField(null=True)
    max_days = models.PositiveIntegerField(null=True)
    receiver = models.ManyToManyField(BusinessProfile,
                                      related_name='service_requests')
    finished = models.BooleanField(default=False)
    skill = models.ManyToManyField(ValidSkill,
                                   related_name='service_requests')
