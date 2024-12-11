from django.shortcuts import render
from testapp.models import Book
from testapp.models import Employee

# Create your views here.

def employee_view(request):
    employees = Employee.objects.all()
    return render(request, 'testapp/result.html', {'employees': employees})

def book_view(request):
    books = Book.objects.all()
    return render(request, 'testapp/result.html', {'books': books})