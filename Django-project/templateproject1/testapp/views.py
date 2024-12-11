from django.http import request
from django.shortcuts import render
import datetime

# Create your views here.

def templates_view(request):
    dt = datetime.datetime.now()
    name, roll_no, marks = 'John', 'ID212', 545 
    dict = {'date': dt, 'Name': name, 'Roll_No': roll_no, 'marks': marks}
    return render(request,'testapp/result.html', context=dict)