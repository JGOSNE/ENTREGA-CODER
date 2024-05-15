from django.shortcuts import render,redirect
from vehiculos.models import vehiculos_list
from vehiculos.forms import vehiculosForms
from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DetailView #CLASE 23 (VISTAS CON CLASES)
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, "index_vehiculos.html")

def vehiculos_mostrar(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = vehiculos_list.objects.filter(Q(marca__icontains=busqueda) | Q(modelo__icontains=busqueda))
    else:
        consulta = vehiculos_list.objects.all()
    contexto = {"vehiculos" : consulta}
    return render(request, "vehiculos_list.html", contexto)


class VehiculoCreate(CreateView):
    model = vehiculos_list
    form_class = vehiculosForms
    success_url = reverse_lazy('vehiculos:listado')
    template_name = "vehiculo_create.html"