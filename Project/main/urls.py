from django.urls import path
from .views import ContactView, HomeView, AboutView, PackagesView, ServicesView, BookingView

urlpatterns = [
    path('', HomeView, name='home'),
    path('about', AboutView, name='about'),
    path('services', ServicesView, name='services'),
    path('packages', PackagesView, name='packages'),
    path('booking/<int:pk>/<int:id>', BookingView, name='booking'),
    path('contact', ContactView, name='contact'),
]