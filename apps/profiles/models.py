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
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=30, blank=True)
    birthday = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=15, choices=GENDER, default='male')