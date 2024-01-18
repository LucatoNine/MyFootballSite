from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


# CONTENU

class Player(models.Model):

    class Position(models.TextChoices):
        DEFENSEUR = 'def'
        MILIEU = 'mil'
        ATTAQUANT = 'att'
        GARDIEN = 'gk'

    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    position = models.fields.CharField(choices=Position.choices, max_length=5)
    year_old = models.fields.IntegerField(validators = [MinValueValidator(16), MaxValueValidator(45)])


    def __str__(self):
        return f'{self.first_name}'
    
# AUTHENTIFICATION
class User(AbstractUser):

    username = None
    USERNAME_FIELD = models.CharField(max_length=63)

    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    
    
