from django.shortcuts import render,redirect
from vehiculos.models import vehiculos_list
from vehiculos.forms import vehiculosForms
from django.db.models import Q

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

def vehiculo_create(request):
    if request.method == "POST":
        form = vehiculosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar:index')
    else:
        form = vehiculosForms()
    return render(request, "vehiculo_create.html", {"form" : form})