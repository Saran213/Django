from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal =models.FloatField()
    eaddr = models.CharField(max_length=64)

    def __str__(self):
        return self.ename

class Book(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=64)
    author =models.CharField(max_length=64)
    published_date = models.DateField()

    def __str__(self):
        return self.title
