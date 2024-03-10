from django.db import models

# Create your models here.

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=25, null=True, blank=False)
    manufacturer = models.CharField(max_length=25, null=True, blank=False)
    engine = models.CharField(max_length=100, null=True, blank=True, default='car')
    fuel = models.CharField(max_length=15, null=True, blank=True, default='car')
    airbags = models.CharField(max_length=20, null=True, blank=True, default='car')
    ground_clearance = models.CharField(max_length=10, null=True, blank=True, default='car')
    gncap_rating = models.CharField(max_length=3, null=True, blank=True, default='car')
    transmission = models.CharField(max_length=20, null=True, blank=True, default='car')
    mileage = models.CharField(max_length=15, null=True, blank=True, default='car')
    boot_space = models.CharField(max_length=10, null=True, blank=True, default='car')
    fuel_tank = models.CharField(max_length=5, null=True, blank=True, default='car')
    adas_level = models.CharField(max_length=5, null=True, blank=True, default='car')
    dashboard = models.CharField(max_length=10, null=True, blank=True, default='car')
    ventilated_seats = models.CharField(max_length=20,null=True, blank=True, default='car')
    
    

