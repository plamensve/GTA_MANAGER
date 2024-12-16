from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
from django.db import models

from GTA_MANAGER.accounts.validators import email_validator


class CustomUser(AbstractUser):
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15
    EMAIL_MAX_LENGTH = 254

    username = models.CharField(
        unique=True,
        max_length=FIRST_NAME_MAX_LENGTH
    )

    email = models.EmailField(
        unique=True,
        max_length=EMAIL_MAX_LENGTH,
        validators=[
            email_validator
        ]
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
