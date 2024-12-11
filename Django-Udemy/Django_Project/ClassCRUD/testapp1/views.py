from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from .models import Registeration
# Create your views here.

class RegisterationCreate(CreateView):
    model = Registeration
    fields = ['fname', 'lname', 'city', 'email']
    success_url = '/list'
    
class RegisterationList(ListView):
    model = Registeration

class RegisterationDetail(DetailView):
    model = Registeration

class RegisterationUpdate(UpdateView):
    model = Registeration
    fields = ['fname', 'lname', 'city', 'email']
    success_url = '/list'

class RegisterationDelete(DeleteView):
    model = Registeration
    success_url = '/list'