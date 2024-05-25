from django.urls import path, include
from core.views import index, CustomLoginView, register
from django.contrib.auth.views import LogoutView

app_name = ""

urlpatterns = [
    path("", index),
    path("personas/", include("personas.urls")),
    path("vehiculos/", include("vehiculos.urls")),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", register, name="register"),
    
    
]