from django.shortcuts import render
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView
# Create your views here.

def index(request):
    return render(request, "index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "login.html"
    
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form":form})

