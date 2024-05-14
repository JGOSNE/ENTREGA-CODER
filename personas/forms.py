from django import forms
from . import models


class personasForms(forms.ModelForm):
    class Meta:
        model = models.personas_list
        fields = ["nombre", "apellido", "vehiculo"]