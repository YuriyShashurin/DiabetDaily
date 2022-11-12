from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(User):

    telegram_id = models.PositiveIntegerField(verbose_name='id телеграм', blank=True, null=True)


class Indication(models.Model):

    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='Пользователь')
    data = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Значение глюкометра')
    date = models.DateField(auto_now=True, verbose_name='Дата')
    time = models.TimeField(auto_now=True, verbose_name='Время')
    comment = models.CharField(max_length=150, verbose_name='Комментарий')

    def __str__(self):
        return f'Показания пользователя {self.user} от {self.date} {self.time}'

