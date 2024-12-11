from django.shortcuts import render, HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('<h2>Welcome to Django World</h2>')

def aboutPageView(request):
    return HttpResponse('<h2 style = "color: red">About Django</h2>')
