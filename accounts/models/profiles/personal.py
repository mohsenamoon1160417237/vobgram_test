from django.db import models
from accounts.models.UserRegistration import UserRegistration
from django.core.validators import MinLengthValidator


class PersonalProfile(models.Model):

    user = models.OneToOneField(UserRegistration, on_delete=models.CASCADE, related_name='personal_profile')
    username = models.CharField(max_length=30,
                                validators=[MinLengthValidator(4)],
                                unique=True,
                                null=True,
                                blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,
                              null=True,
                              blank=True)

    def __str__(self):

        return self.user
