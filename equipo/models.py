from django.db import models


# Create your models here.
class Catastrofe(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.IntegerField()
    estado = models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=150)

class Clima(models.Model):
    id = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=150)
    temperatura = models.FloatField()
    precipitacion = models.CharField(max_length=50)
    viento = models.FloatField()
    resumen = models.CharField(max_length=150)
    lat = models.FloatField()
    lon = models.FloatField()
