from django.shortcuts import render, HttpResponse

# Create your views here.
def homePageView(request):
    h1 = '<h1>Welcome To Django World</h1>'
    return HttpResponse(h1)

def aboutPageView(request):
    h1 = '<h1>About US</h1>'
    return HttpResponse(h1)

def servicePageView(request):
    h1 = '<h1>Sevices World</h1>'
    return HttpResponse(h1)

def contactPageView(request):
    h1 = '<h1>Contact World</h1>'
    return HttpResponse(h1)