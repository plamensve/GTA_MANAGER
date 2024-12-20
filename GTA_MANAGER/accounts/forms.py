from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from GTA_MANAGER.accounts.models import Vehicles, CustomUser, VehicleFullDetails


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        error_messages = {
            'username': {
                'required': "Моля, въведете потребителско име.",
                'unique': "Това потребителско име вече е заето.",
            },
            'email': {
                'required': "Моля, въведете имейл адрес.",
                'unique': "Този имейл вече е регистриран.",
            }
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True}),
        label="Потребителско име"
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Парола"
    )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')  # Само тези полета

        labels = {
            'username': 'Потребителско име',
            'first_name': 'Име',
            'last_name': 'Фамилия',
            'email': 'E-mail',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            del self.fields['password']


class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = '__all__'

        labels = {
            'type': '',
            'brand': '',
            'model': '',
            'register_number': '',
            'condition': '',
        }

        widgets = {
            'type': forms.Select(attrs={'placeholder': 'Изберете тип'}),
            'brand': forms.TextInput(attrs={'placeholder': 'Марка на превозното средство'}),
            'model': forms.TextInput(attrs={'placeholder': 'Модел на превозното средство'}),
            'register_number': forms.TextInput(attrs={'placeholder': 'Регистрационен номер'}),
            'condition': forms.Select(attrs={'placeholder': 'Състояние'}),
            'adr': forms.Select(attrs={'placeholder': 'ADR'})
        }

    def clean_register_number(self):
        register_number = self.cleaned_data.get('register_number')

        if Vehicles.objects.filter(register_number=register_number).exists():
            raise ValidationError('Превозно средство с този регистрационен номер вече съществува.')

        return register_number


class VehicleFullDetailsCreateForm(forms.ModelForm):
    class Meta:
        model = VehicleFullDetails
        fields = '__all__'

        labels = {
            'wheel_chock': 'Kлинове',
            'two_warning_signs': '2 бр. знаци',
            'eye_wash_liquid': 'Течност за промивка',
            'reflective_vest': 'Жилетка',
            'portable_lighting_fixture': 'Фенер',
            'a_pair_of_protective_gloves': 'Ръкавици',
            'eye_protection': 'Очила',
            'mask': 'Маска',
            'shovel': 'Лопата',
            'manhole_cover': 'Покривало',
            'collection_container': 'Контейнер',
            'written_instructions_colored': 'Писмени инструкции',
            'fire_extinguishers': 'Пожарогасители',
            'insurance_civil_liability': 'Застраховка ГО',
            'insurance_casco_validity': 'Застраховка КАСКО',
            'tachograph_validity': 'Тахограф',
            'adr_validity': 'АДР',
            'fitness_protocol_validity': 'Протокол за годност',
            'technical_check_validity': 'Технически преглед'
        }

        widgets = {
            'insurance_civil_liability': forms.DateInput(attrs={
                'type': 'text',
                'class': 'form-control flatpickr-date',
                'placeholder': 'dd/mm/yyyy'
            }),
            'insurance_casco_validity': forms.DateInput(attrs={
                'type': 'text',
                'class': 'form-control flatpickr-date',
                'placeholder': 'dd/mm/yyyy'
            }),
            'tachograph_validity': forms.DateInput(attrs={
                'type': 'text',
                'class': 'form-control flatpickr-date',
                'placeholder': 'dd/mm/yyyy'
            }),
            'adr_validity': forms.DateInput(attrs={
                'type': 'text',
                'class': 'form-control flatpickr-date',
                'placeholder': 'dd/mm/yyyy'
            }),
            'fitness_protocol_validity': forms.DateInput(attrs={
                'type': 'text',
                'class': 'form-control flatpickr-date',
                'placeholder': 'dd/mm/yyyy'
            }),
            'technical_check_validity': forms.DateInput(attrs={
                'type': 'text',
                'class': 'form-control flatpickr-date',
                'placeholder': 'dd/mm/yyyy'
            }),
            'wheel_chock': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'two_warning_signs': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'eye_wash_liquid': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'reflective_vest': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'portable_lighting_fixture': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'a_pair_of_protective_gloves': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'eye_protection': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'mask': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'shovel': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'manhole_cover': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'collection_container': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'written_instructions_colored': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
            'fire_extinguishers': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Изберете опция'
            }),
        }
