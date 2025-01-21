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

    is_active = models.BooleanField(
        default=False,
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

    CONDITION_CHOICES = [
        ('АКТИВЕН', 'АКТИВЕН'),
        ('В РЕМОНТ', 'В РЕМОНТ'),
    ]

    ADR_CHOICES = [
        ('Да', 'Да'),
        ('Не', 'Не')
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
        max_length=REGISTER_NUMBER_MAX_LENGTH,
        validators=[
            MinLengthValidator(REGISTER_NUMBER_MIN_LENGTH),
        ],
        unique=True,
    )

    condition = models.CharField(
        max_length=CONDITION_MAX_LENGTH,
        choices=CONDITION_CHOICES,
        default='АКТИВЕН'
    )

    adr = models.CharField(
        choices=ADR_CHOICES,
        default='Да'
    )

    comp = models.IntegerField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.pk:  # Проверка дали обектът вече съществува
            old_instance = Vehicles.objects.filter(pk=self.pk).first()
            if old_instance and old_instance.comp and self.comp is None:
                self.comp = old_instance.comp  # Запазване на старата стойност на comp
        super().save(*args, **kwargs)


class VehicleFullDetails(models.Model):
    DETAILS_CHOICE = [
        ('Да', 'Да'),
        ('Не', 'Не')
    ]

    wheel_chock = models.CharField(
        choices=DETAILS_CHOICE,
        default='Нe',
        blank=True
    )

    two_warning_signs = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    eye_wash_liquid = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    reflective_vest = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    portable_lighting_fixture = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    a_pair_of_protective_gloves = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    eye_protection = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    mask = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    shovel = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    manhole_cover = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    collection_container = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    written_instructions_colored = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    fire_extinguishers = models.CharField(
        choices=DETAILS_CHOICE,
        default='Не',
        blank=True
    )

    insurance_civil_liability = models.DateField(
        null=True,
        blank=True
    )

    insurance_casco_validity = models.DateField(
        null=True,
        blank=True
    )

    tachograph_validity = models.DateField(
        null=True,
        blank=True
    )

    adr_validity = models.DateField(
        null=True,
        blank=True
    )

    fitness_protocol_validity = models.DateField(
        null=True,
        blank=True
    )

    technical_check_validity = models.DateField(
        null=True,
        blank=True
    )

    vehicle = models.ForeignKey(
        Vehicles,
        on_delete=models.CASCADE,
        related_name='full_details',
        null=True,
        blank=True
    )

    @property
    def formatted_insurance_civil_liability(self):
        if self.insurance_civil_liability:
            return self.insurance_civil_liability.strftime('%d-%m-%Y')
        return "Няма данни"

    @property
    def formatted_insurance_casco_validity(self):
        if self.insurance_casco_validity:
            return self.insurance_casco_validity.strftime('%d-%m-%Y')
        return "Няма данни"

    @property
    def formatted_tachograph_validity(self):
        if self.tachograph_validity:
            return self.tachograph_validity.strftime('%d-%m-%Y')
        return "Няма данни"

    @property
    def formatted_adr_validity(self):
        if self.adr_validity:
            return self.adr_validity.strftime('%d-%m-%Y')
        return "Няма данни"

    @property
    def formatted_fitness_protocol_validity(self):
        if self.fitness_protocol_validity:
            return self.fitness_protocol_validity.strftime('%d-%m-%Y')
        return "Няма данни"

    @property
    def formatted_technical_check_validity(self):
        if self.technical_check_validity:
            return self.technical_check_validity.strftime('%d-%m-%Y')
        return "Няма данни"