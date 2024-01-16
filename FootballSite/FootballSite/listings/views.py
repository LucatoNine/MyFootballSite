from django.shortcuts import render
from django.http import HttpResponse
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
