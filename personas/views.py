from django.shortcuts import render, redirect
from personas.forms import personasForms
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request, "index_personas.html")

@login_required(login_url='/login/')
def persona_create(request):
    if request.method == "POST":
        form = personasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar:index')
    else:
        form = personasForms()
    return render(request, "persona_create.html", {"form" : form})



