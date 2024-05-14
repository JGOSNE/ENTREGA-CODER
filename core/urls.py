from django.urls import path, include
from . import views

app_name = ""

urlpatterns = [
    path("", views.index),
    path("personas/", include("personas.urls")),
    path("vehiculos/", include("vehiculos.urls")),
    
    
]