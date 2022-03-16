from django.db import models

from accounts.models.UserRegistration import UserRegistration


class BusinessSpecialty(models.Model):

    user = models.ForeignKey(UserRegistration,
                             on_delete=models.CASCADE,
                             related_name='business_specialties')
    title = models.CharField(max_length=300)
    note = models.TextField()
    education_institute_name = models.CharField(max_length=150)

    class Meta:

        unique_together = [('user', 'title')]
