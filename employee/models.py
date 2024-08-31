from datetime import timedelta

from django.db import models
from django.utils import timezone


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50, default='NA')

    phone_number = models.CharField(max_length=15, unique=True, blank=False)
    is_phone_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    date_joined = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


