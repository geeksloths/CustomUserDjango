# Generated by Django 3.2.6 on 2021-08-30 23:07

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='ایمیل')),
                ('username', models.CharField(max_length=16, unique=True, verbose_name='نام کاربری')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='آخرین تاریخ ورود')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, default=account.models.get_default_profile_image, max_length=255, null=True, upload_to=account.models.get_profile_image_filepath)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
