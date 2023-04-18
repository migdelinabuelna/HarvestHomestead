from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    preferred_living_conditions = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

class Farm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 150)
    date = models.DateField(auto_now=True)
    vote = models.IntegerField(default=0)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for animal_id {self.animal_id} @{self.url}'
    
class Crops(models.Model):
    name = models.CharField(max_length=50)
    water_dependancy = models.IntegerField()
    growing_season = models.CharField(max_length=10)
    optimal_growing_conditions = models.CharField(max_length=100)
    average_growth_time = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

FUEL_TYPE = (
    ('G', 'Gasoline'),
    ('D', 'Diesel'),
    ('K', 'Kerosene'),
    ('L', 'LP Gas'),
)

class Equipment(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    hydraulic_rating = models.IntegerField()
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    fuel_type = models.CharField(max_length=1, choices=FUEL_TYPE, default=FUEL_TYPE[0][0])
    engine_information = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


