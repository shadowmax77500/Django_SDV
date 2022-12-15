from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User_WebSite(models.Model):
    """Cette classe va se composer de différents attributs:
    - username
    - adresse électronique
    - mot de passe
    """
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)