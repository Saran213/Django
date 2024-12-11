from django.shortcuts import render, HttpResponse

# Create your views here.

def f1(request):
    h1 = '<h1>F1() Works</h1>'
    return HttpResponse(h1)