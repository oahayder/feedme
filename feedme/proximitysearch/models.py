from django.db import models

class FoodFacility(models.Model):
    permitId = models.TextField()
    name = models.TextField()
    address = models.TextField()
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    scheduleLink = models.TextField()
    status = models.TextField(default='')
    lastUpdatedTimestamp = models.DateField(auto_now=True)
    distance=0


    def __unicode__(self):
        return self.name

    def set_distance(self, distance):
        self.distance = distance
