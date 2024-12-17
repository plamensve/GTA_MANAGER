from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from GTA_MANAGER.accounts.validators import email_validator


class CustomUser(AbstractUser, PermissionsMixin):
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


class Vehicles(models.Model):
    REGISTER_NUMBER_MIN_LENGTH = 6
    REGISTER_NUMBER_MAX_LENGTH = 8
    CONDITION_MAX_LENGTH = 50

    TYPE_CHOICES = [
        ('ВЛЕКАЧ', 'ВЛЕКАЧ'),
        ('ЦИСТЕРНА', 'ЦИСТЕРНА'),
        ('АВТОМОБИЛ', 'АВТОМОБИЛ'),
    ]

    type = models.CharField(
        choices=TYPE_CHOICES,
        default='АВТОМОБИЛ'
    )

    brand = models.CharField(

    )

    model = models.CharField(

    )

    register_number = models.CharField(
        validators=[
            MinLengthValidator(REGISTER_NUMBER_MIN_LENGTH),
            MaxLengthValidator(REGISTER_NUMBER_MAX_LENGTH)
        ]
    )

    condition = models.TextField(
        validators=[
            MaxLengthValidator(CONDITION_MAX_LENGTH)
        ]
    )
