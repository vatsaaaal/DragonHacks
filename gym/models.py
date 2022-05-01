from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Gym(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    contact = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/')
    gym = models.ManyToManyField(Gym)

    def __str__(self):
        return self.name

class Muscle(models.Model):
    name = models.CharField(max_length=100)
    equipment = models.ManyToManyField(Equipment)

    def __str__(self):
        return self.name