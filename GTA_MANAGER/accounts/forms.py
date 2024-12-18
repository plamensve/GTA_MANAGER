from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from GTA_MANAGER.accounts.models import Vehicles, CustomUser


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
            'email': 'Имейл',
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
        }





















