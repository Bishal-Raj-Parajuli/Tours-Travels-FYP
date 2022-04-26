from importlib.resources import Package
from multiprocessing import context
from django.shortcuts import render
from .models import Bookings, Destinations, Guides, Packages
from django.core.mail import send_mail

# Create your views here.
def HomeView(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Packages.objects.filter(destination__name__contains=search)
        context = {
            'results': results
        }
        return render(request, 'main/home.html', context)
    else:
        context = {
            'results': ''
        }
        return render(request, 'main/home.html', context)

def Dashboard(request):
    user = request.user
    details = Bookings.objects.filter(user=user)
    context = {
        'details':details
    }
    return render(request, 'main/user-dashboard.html', context)

def AboutView(request):
    guides = Guides.objects.filter(is_active=True)
    context = {
        'guides':guides,
    }
    return render(request, 'main/about.html', context)

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
    
    if request.method == 'POST':
        if request.POST.get('hire_guide') == 'on':
            object = Packages.objects.get(pk=pk)
            guides = Guides.objects.filter(is_active=True)
            context = {
                'object':object,
                'guides': guides
            }
            return render(request, 'main/hire-guide.html', context)
        else:
            package = Packages.objects.get(pk=pk)
            user = request.user
            booking = Bookings(package=package, user=user)
            booking.save()
            # Sending Mail
            send_mail(
                'Package Booked Successfully',#subject
                f"Your Package for {package.destination.name} Has been successfully booked. You will receive a call from our office Shortly. Your total amount for this package is Rs. {package.price}",#message
                'srijanthapaliya111@gmail.com',#from email
                [user.email],#to email

            )
            context = {
                'package':package
            }
            return render(request, 'main/booked.html', context)
        

def BookedGuideView(request, id, pk):
    if request.method == 'GET':
        guide = Guides.objects.get(pk=pk)
        package = Packages.objects.get(pk=id)
        user = request.user
        booking = Bookings(package = package, user=user, guide=guide)
        booking.save()
        context = {
            'package': package,
            'user': user,
            'guide': guide,
        }
        return render(request, 'main/booked-guide.html', context)

def ContactView(request):
    return render(request, 'main/contact.html')