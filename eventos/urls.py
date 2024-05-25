from django.urls import path
from eventos.views import Eventos_list

app_name = "eventos"

urlpatterns = [
    path("", Eventos_list, name="listado"),
    
]