from django import http
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.

def date_time(request):
    date = dt.datetime.now()
    s = '<h1> The current date and time at server is: ' + str(date) + '</h1>'
    return HttpResponse(s)