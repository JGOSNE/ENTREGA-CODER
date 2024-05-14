from django.urls import path
from . import views

app_name = "vehiculos"

urlpatterns = [
    path("", views.index, name="index"),
    path("vehiculos_list/", views.vehiculos_mostrar, name="listado"),
    
]

#35 min
# 2h 5m