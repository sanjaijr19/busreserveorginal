from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)




# Create your models here.
class Driver(models.Model):
    drivername=models.CharField(max_length=20)
    age=models.IntegerField()
    contact_no=models.IntegerField()
    bus_no=models.IntegerField()

    # def __str__(self):
    #     return drivername


class Customer(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.TextField()
    phone=models.PositiveBigIntegerField()
    start=models.CharField(max_length=30)
    end=models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()









from django.contrib.auth.models import Group

class MyModel(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
