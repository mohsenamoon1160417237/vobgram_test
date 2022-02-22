from django.db import models

from accounts.models.profiles.business import BusinessProfile


class BusinessSpecialty(models.Model):

    business_profile = models.ForeignKey(BusinessProfile,
                                         on_delete=models.CASCADE,
                                         related_name='business_specialties')
    title = models.CharField(max_length=300)
    note = models.TextField()
    education_institute_name = models.CharField(max_length=150)

    class Meta:

        unique_together = [('business_profile', 'title')]
