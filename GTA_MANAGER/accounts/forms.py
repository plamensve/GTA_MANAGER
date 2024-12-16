from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


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
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = '__all__'
