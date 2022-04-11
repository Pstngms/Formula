# Generated by Django 4.0.3 on 2022-04-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='vk_link',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Ссылка на профиль VK'),
        ),
    ]