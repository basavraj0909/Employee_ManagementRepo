from django.conf import settings

from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, blank=False)
    is_phone_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.username


class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    position = models.CharField(max_length=50, default='NA')
    date_joined = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


