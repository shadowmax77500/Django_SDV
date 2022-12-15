from django.db import models

# Create your models here.
class Personnage(models.Model):
    nom = models.CharField(max_length=128)
    force = models.TextField(blank=True)
    combats_gagnes = models.IntegerField(default=0)
    combats_perdus = models.IntegerField(default=0)