from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greetings(request):
    return HttpResponse('<h1>Hello! Good morning... Have a nice day</h1>')