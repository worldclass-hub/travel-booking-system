from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_travel_agent = models.BooleanField(default=False)

    def __str__(self):
        return self.username
