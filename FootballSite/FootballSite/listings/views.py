from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from . import forms

# Create your views here.

# Page d'accueil
def home(request):
    return render(request, 'listings/home.html')

# Page de présentation

def about(request):
    return render(request, 'listings/about.html')

# Page projet

def project(request):
    return render(request, 'listings/project.html')

# Page contact

def contact(request):
    return render(request, 'listings/contact.html')

# Page de connexion

def login_page(request):
    form = forms.loginForm()
    message = ''
    if request.method == 'POST':
        form = forms.loginForm(request.POST)
        if form.is_valid():
            user = authenticate( 
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is None:
                login(request, user)
                message = f'Bonjour {user.username}, vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'listings/login.html', context={'form': form, 'message': message})
    
