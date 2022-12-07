from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthdate = models.DateField(auto_now=False, null=True, blank=True)
    is_employee = models.BooleanField(default=False)
    date_joined = None
    is_active = None
    last_login = None
