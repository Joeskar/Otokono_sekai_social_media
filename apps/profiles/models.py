from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model"""
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    )

    middle_name = models.CharField(max_length=30, verbose_name='Отчество')
    first_login = models.DateTimeField(blank=True, null=True)
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True, verbose_name='Аватарка')
    bio = models.TextField(blank=True, null=True, verbose_name='Ава')
    github = models.CharField(max_length=30, blank=True)
    birthday = models.DateTimeField(blank=True, null=True, verbose_name='День рождение')
    gender = models.CharField(max_length=15, choices=GENDER, default='male')
