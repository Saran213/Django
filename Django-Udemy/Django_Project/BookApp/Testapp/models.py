from django.db import models

# Create your models here.
class BookRegister(models.Model):
    bname = models.CharField(max_length=50)
    aname = models.CharField(max_length=50)
    pname = models.CharField(max_length=50)
    pyear = models.CharField(max_length=50)