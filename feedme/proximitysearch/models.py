from math import radians, cos, sin, asin, sqrt

from django.db import models

class FoodFinderInfo(models.Model):
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

    def get_distance_from(self, longitude, latitude):

        # In miles
        # TODO read the desired metric setting from UserConfig
        earth_radius = 3963.1676


        # Uses the Haversine Formula (http://en.wikipedia.org/wiki/Haversine_formula)
        lon1, lat1, lon2, lat2 = map(radians, [self.longitude, self.latitude, longitude, latitude])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))

        distance = earth_radius * c

        return distance
