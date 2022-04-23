from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


class Events(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/events/%Y/%m/%d', blank=True, verbose_name='Фото')
    start_date = models.DateTimeField(verbose_name='Начало')
    finish_date = models.DateTimeField(blank=True, null=True,verbose_name='Конец')
    communication = models.TextField(blank=True, verbose_name='Контакты')
    location = models.TextField(blank=True, verbose_name='Место проведения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')

    def get_absolute_url(self):
        return reverse('view_events', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class EventsRegistration(models.Model):
    event = models.ForeignKey(Events, on_delete=models.SET_NULL, null=True, verbose_name='Мероприятие')
    user_email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   verbose_name='Пользователь')
    is_registered = models.BooleanField(default=False, verbose_name='Зарегистрирован?')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации')


    def __str__(self):
        return f'{self.user_email}:{self.event} {self.is_registered}'
    class Meta:
        verbose_name = 'Регистрация на мероприятие'
        verbose_name_plural = 'Регистрация на мероприятия'
