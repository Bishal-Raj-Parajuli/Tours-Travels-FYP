from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'main/home.html')

def AboutView(request):
    return render(request, 'main/about.html')

def ServicesView(request):
    return render(request, 'main/services.html')

def PackagesView(request):
    return render(request, 'main/packages.html')

def ContactView(request):
    return render(request, 'main/contact.html')