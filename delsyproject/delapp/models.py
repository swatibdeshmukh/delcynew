
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phoneNo = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="images/", blank=True, null=True)

class Experience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='experience')
    companyName = models.CharField(max_length=100)
    fromDate = models.CharField(max_length=50)
    toDate = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class AddressDetails(models.Model):#dictinaonry obj #one to one
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='addressDetails')
    hno = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

class Qualification(models.Model):
    employee =  models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='qualification')
    qualificationName = models.CharField(max_length=50)
    percentage = models.FloatField()

class Project(models.Model):#list of dict#foreignkey
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='project')
    title = models.CharField(max_length=50)
    description = models.TextField()

