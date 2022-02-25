from telnetlib import STATUS
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    STATUS = (
        ('available', 'available'),
        ('booked', 'booked'),
        ('unavailable', 'unavailable'),
    )
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class RentVehicle(models.Model):
    STATUS = (
        ('new', 'new'),
        ('booked', 'booked'),
        ('expire', 'expire'),

    )
    # vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    useremail = models.EmailField(max_length=200)
    usermobile = models.CharField(max_length=15)
    status = models.CharField(max_length=200, choices=STATUS, default='new')
    rental_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.vehicle