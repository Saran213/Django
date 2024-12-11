from django.contrib import admin
from testapp.models import Employee, Book

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno', 'ename', 'esal', 'eaddr']

class BookAdmin(admin.ModelAdmin):
    list_display=['id', 'number','title', 'author', 'published_date']    

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Book, BookAdmin)