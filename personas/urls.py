from django.urls import path
from .views import persona_create, index
from vehiculos.views import VehiculoCreate

app_name = "registrar"

urlpatterns = [
    path("", index, name="index"),
    path("persona_create/", persona_create ,name="persona"),
    path("vehiculo_create/", VehiculoCreate.as_view(), name="vehiculo"),
]
