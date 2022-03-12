from importlib.resources import Package
from django.shortcuts import render
from .models import Destinations, Packages

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

def BookingView(request, pk, id):
    if request.method == 'GET':
        object = Packages.objects.get(pk=pk)
        context = {
            'object':object
        }
        return render(request, 'main/book-package.html', context)

def ContactView(request):
    return render(request, 'main/contact.html')