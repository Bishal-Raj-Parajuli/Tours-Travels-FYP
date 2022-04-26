from django.urls import path
from .views import ContactView, HomeView, AboutView, PackagesView, ServicesView, BookingView, BookedGuideView, Dashboard

urlpatterns = [
    path('', HomeView, name='home'),
    path('user-dashboard', Dashboard, name='dashboard'),
    path('about', AboutView, name='about'),
    path('services', ServicesView, name='services'),
    path('packages', PackagesView, name='packages'),
    path('booking/<int:pk>/<int:id>', BookingView, name='booking'),
    path('booked-hire/<int:id>/<int:pk>', BookedGuideView, name='booked-guide'),
    path('contact', ContactView, name='contact'),
]