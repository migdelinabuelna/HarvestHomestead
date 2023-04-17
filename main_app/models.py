from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    preferred_living_conditions = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

class Farm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
