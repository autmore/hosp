from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from hospital.models import CustomUser


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=15,
        required=True,
        label="Имя пользователя",
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя', 'class': 'form-field'}),
    )

    phone_number = forms.CharField(
        max_length=15,
        required=True,
        label="Телефон",
        widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона', 'class': 'form-field'}),
    )

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Введите email', 'class': 'form-field'}),
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-field'}),
    )

    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': 'form-field'}),
    )

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'password1', 'password2')
        labels = {
            'username': 'Имя пользователя',
        }

class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(
        max_length=15,
        required=True,
        label="Имя пользователя",
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя', 'class': 'form-field'}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-field'}),
    )
    class Meta:
        model = User
        fields = ('username', 'password')




