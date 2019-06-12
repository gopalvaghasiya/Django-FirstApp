from django.db import models

# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length=100)
    emailId = models.CharField(max_length=100)
    DOB = models.DateField()
    companyName = models.CharField(max_length=100)
    joinDate = models.DateField()


