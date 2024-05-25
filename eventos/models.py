from django.db import models
from vehiculos.models import vehiculos_list

# Create your models here.

class Evento(models.Model):
    ubicacion = models.CharField(max_length=30)
    fecha = models.DateField()
    cant_entradas = models.IntegerField()
    autos = models.ManyToManyField(vehiculos_list)
    
    def __str__(self):
        return f"{self.ubicacion} - {self.fecha}"
