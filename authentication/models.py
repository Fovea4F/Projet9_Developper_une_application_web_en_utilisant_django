from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    follows = models.ManyToManyField('self', symmetrical=False, verbose_name='Personnes suivies')
