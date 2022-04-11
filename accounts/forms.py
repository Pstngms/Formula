from django import forms

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'patronymic')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(CustomUserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    patronymic = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))


class UserUpdateForm(CustomUserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    patronymic = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))



