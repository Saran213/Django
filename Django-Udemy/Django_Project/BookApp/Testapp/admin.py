from django.contrib import admin
from .models import BookRegister
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['bname', 'aname', 'pname', 'pyear']

admin.site.register(BookRegister, RegisterAdmin)
