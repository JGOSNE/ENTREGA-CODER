from django.db import models

# Create your models here.

class personas_list(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    vehiculo = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"
    