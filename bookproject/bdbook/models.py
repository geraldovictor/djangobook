from django.db import models
from rest_framework import viewsets
# Create your models here.

class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=36, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    desc = models.TextField(max_length=256, blank=True)
    date = models.DateField(auto_now_add=True)
    number = models.OneToOneField(BookNumber,null=True,blank=True,on_delete= models.CASCADE)
    def __str__(self):
        return self.title

