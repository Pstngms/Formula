from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name='Отчество')
    phone = models.CharField(max_length=50, blank=True, null=True,default='', verbose_name='Номер телефона')
    vk_link = models.CharField(max_length=200, blank=True, null=True,default='', verbose_name='Ссылка на профиль VK')
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False, verbose_name='Модератор?')
    is_active = models.BooleanField(default=True, verbose_name='Активный?')
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.email}'

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

