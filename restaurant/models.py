from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)  


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    
    
    def __str__(self):
        return f"Booking by {self.user.username} on {self.date} at {self.time}"
    