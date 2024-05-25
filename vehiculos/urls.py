from django.urls import path
from vehiculos.views import index, vehiculos_mostrar, VehiculoDetail, VehiculoDelete

app_name = "vehiculos"

urlpatterns = [
    path("", index, name="index"),
    path("vehiculos_list/", vehiculos_mostrar, name="listado"),
    path("vehiculos_Detail/<int:pk>", VehiculoDetail, name="detail"),
    path("vehiculos_delete/<int:pk>", VehiculoDelete, name="borrar"),
    
]

