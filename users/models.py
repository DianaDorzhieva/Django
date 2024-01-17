from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    DoesNotExist = None
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='телефон')
    county = models.CharField(max_length=50, verbose_name='страна')
    email_verification_token = models.CharField(max_length=255, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
