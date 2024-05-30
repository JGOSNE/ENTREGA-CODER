from django.shortcuts import render,redirect
from vehiculos.models import vehiculos_list
from vehiculos.forms import vehiculosForms
from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DetailView #CLASE 23 (VISTAS CON CLASES)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request, "index_vehiculos.html")

@login_required(login_url='/login/')
def vehiculos_mostrar(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = vehiculos_list.objects.filter(Q(marca__icontains=busqueda) | Q(modelo__icontains=busqueda))
    else:
        consulta = vehiculos_list.objects.all()
    contexto = {"vehiculos" : consulta}
    return render(request, "vehiculos_list.html", contexto)


class VehiculoCreate(LoginRequiredMixin, CreateView):
    model = vehiculos_list
    form_class = vehiculosForms
    success_url = reverse_lazy('registrar:index')
    template_name = "vehiculo_create.html"
    login_url = '/login/'

@login_required(login_url='/login/')
def VehiculoDetail(request, pk:int):
    consulta = vehiculos_list.objects.get(id=pk)
    contexto = {"vehiculo" : consulta}
    return render(request, "vehiculo_detail.html", contexto)

@login_required(login_url='/login/')
def VehiculoDelete(request, pk:int):
    consulta = vehiculos_list.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("vehiculos:listado")
    return render(request, "vehiculos_confirm_delete.html", {"object" : consulta})

    