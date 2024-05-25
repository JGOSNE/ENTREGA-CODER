from django.shortcuts import render
from eventos.models import Evento

# Create your views here.

def Eventos_list(request):
    eventos = Evento.objects.all()
    return render(request, "index_eventos.html", {"eventos":eventos})
