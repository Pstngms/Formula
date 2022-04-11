from django.db import models


class Contact(models.Model):
    name = models.TextField(max_length=150, verbose_name='Имя')
    email = models.TextField(max_length=150, verbose_name='Email')
    phone = models.TextField(max_length=150, verbose_name='Телефон')
    message = models.TextField(verbose_name='Начало')
    is_processed = models.BooleanField(default=False, blank=True, verbose_name='Обработан?')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
