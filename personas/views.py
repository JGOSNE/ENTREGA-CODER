from django.shortcuts import render, redirect
from personas.forms import personasForms

# Create your views here.

def index(request):
    return render(request, "index_personas.html")

def persona_create(request):
    if request.method == "POST":
        form = personasForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar:index')
    else:
        form = personasForms()
    return render(request, "persona_create.html", {"form" : form})



