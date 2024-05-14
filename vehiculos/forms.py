from django import forms
from . import models

class vehiculosForms(forms.ModelForm):
    class Meta:
        model = models.vehiculos_list
        fields = ["marca", "modelo", "propietario"]