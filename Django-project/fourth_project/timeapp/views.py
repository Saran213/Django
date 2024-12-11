from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.

def time_info(request):
    time = dt.datetime.now()
    s = '<h1>Current Time is: ' + str(time) + '</h1>'
    return HttpResponse(s)