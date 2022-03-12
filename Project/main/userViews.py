from turtle import home
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.contrib import messages

from .models import CustomUser
from .userForms import RegistrationForm


class RegistrationView(CreateView):
    template_name = 'core/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)
        return success_url

class ProfileView(UpdateView):
    model = CustomUser
    fields = ['name', 'phone', 'date_of_birth', 'picture']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user

def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request=request, user=user)
            return render(request, 'main/home.html')
        else:
            return HttpResponse('Sorry Something Went Wrong !!!')
    else:
        return render(request, 'core/login.html')

def LogoutView(request):
    user = request.user
    print(user)
    logout(request)
    return render(request, 'main/home.html', {'message':'Successfully Logged Out !!!'})
    