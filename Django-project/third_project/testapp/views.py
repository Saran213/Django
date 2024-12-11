from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def good_morning(request):
    return HttpResponse('<h1>Hello! Good morning...')

def good_afternoon(request):
    return HttpResponse('<h1>Hello! Good afternoon...')

def good_evening(request):
    return HttpResponse('<h1>Hello! Good evening...')