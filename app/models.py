from django.db import models

# Create your models here.
class Admin(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=100)
    Contact=models.CharField(max_length=100)  
