from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import BookRegister
# Create your views here.

class BookCreate(CreateView):
    model = BookRegister
    fields = ['bname', 'aname', 'pname', 'pyear']