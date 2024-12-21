from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-signin', "id": "password"}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-signin', "id": "password"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-signin'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-signin'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-signin'}),
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={"class": 'form-signin'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": 'form-signin'}))
