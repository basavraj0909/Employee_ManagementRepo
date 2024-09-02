from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.conf import settings

import random
import string


class OTP(models.Model):
    """
    Model representing a One-Time Password (OTP) associated with an Employee.
    Attributes:
        registration (Employee): The registration to whom the OTP is associated.
        otp (str): A 6-character string representing the OTP.
        created_at (datetime): The date and time when the OTP was created.
        expires_at (datetime): The date and time when the OTP will expire.
    Methods:
        save(*args, **kwargs): Overrides the default save method to set the expiration time if not provided.
        is_expired() -> bool: Returns True if the OTP is expired, otherwise False.
    """
    phone_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=5)  # Example expiration time
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expires_at
