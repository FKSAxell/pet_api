from django.utils import timezone

from django.db import models

# Create your models here.

#nombre
#edad
#color
#raza
class Animales(models.Model):
    nombre=models.CharField(max_length=200)
    edad=models.IntegerField()
    color=models.CharField(max_length=200)
    raza=models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)


