from django.contrib import admin
from .models import Registeration
# Register your models here.

class RegisterationAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'city', 'email']

admin.site.register(Registeration, RegisterationAdmin)