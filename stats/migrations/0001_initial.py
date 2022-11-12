# Generated by Django 4.1.3 on 2022-11-12 09:02

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telegram_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='id телеграм')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Indication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Значение глюкометра')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата')),
                ('time', models.TimeField(auto_now=True, verbose_name='Время')),
                ('comment', models.CharField(max_length=150, verbose_name='Комментарий')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.userprofile', verbose_name='Пользователь')),
            ],
        ),
    ]
