from django.db import models

# Create your models here.

class Registeration(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    email = models.CharField(max_length=30)