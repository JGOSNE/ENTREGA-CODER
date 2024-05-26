from django.shortcuts import render
from eventos.models import Evento
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def Eventos_list(request):
    eventos = Evento.objects.all()
    return render(request, "index_eventos.html", {"eventos":eventos})
