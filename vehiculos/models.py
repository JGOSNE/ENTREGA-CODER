from django.db import models
from personas.models import personas_list

# Create your models here.

class vehiculos_list(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    propietario = models.ForeignKey(personas_list, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="vehiculos", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.modelo