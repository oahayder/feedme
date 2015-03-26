from django.db import models

class Display(models.Model):
    name = models.TextField()
    image = models.ImageKey()
    address = models.TextField()
    description = models.TextField()

class Coordinates(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

class Schedule(models.Model):
    link = models.TextField()