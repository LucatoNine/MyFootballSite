from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Page d'accueil
def home(request):
    return (request, 'listings/home.html')

# Page de présentation

def about(request):
    return (request, 'listings/about.html')

# Page projet

def project(request):
    return (request, 'listings/project.html')

# Page contact

def contact(request):
    return (request, 'listings/contact.html')