from importlib.resources import Package
from django.shortcuts import render
from .models import Packages

# Create your views here.
def HomeView(request):
    return render(request, 'main/home.html')

def AboutView(request):
    return render(request, 'main/about.html')

def ServicesView(request):
    return render(request, 'main/services.html')

def PackagesView(request):
    objects = Packages.objects.filter(is_active=True)
    context = {
        'objects':objects
    }
    return render(request, 'main/packages.html', context)

def ContactView(request):
    return render(request, 'main/contact.html')