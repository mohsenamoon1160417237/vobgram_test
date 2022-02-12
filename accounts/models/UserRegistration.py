from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

class UserRegistration(AbstractBaseUser):

    phone_number = models.CharField(max_length=12, unique=True)
    user_type = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    registered = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'

    def __str__(self):

        return self.phone_number
