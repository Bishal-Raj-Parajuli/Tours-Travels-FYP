from django.urls import path
from .views import ContactView, HomeView, AboutView, PackagesView, ServicesView

urlpatterns = [
    path('', HomeView, name='home'),
    path('about', AboutView, name='about'),
    path('services', ServicesView, name='services'),
    path('packages', PackagesView, name='packages'),
    path('booking/<int:pk>', PackagesView, name='packages'),
    path('contact', ContactView, name='contact'),
]