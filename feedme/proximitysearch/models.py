import math
from django.db import models

class FoodFinderInfo(models.Model):
    permitId = models.TextField()
    name = models.TextField()
    address = models.TextField()
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    scheduleLink = models.TextField()
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
        delta_y = self.longitude - longitude
        delta_x = self.latitude - latitude
        a = math.pow((math.sin(delta_x/2)),2) + math.cos(latitude) * math.cos(self.latitude) * math.pow((math.sin(delta_y/2)),2)
        c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a) )
        distance = earth_radius * c

        return distance

class UserInfo(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __unicode__(self):
        return self.name

    # This will return the grid point for this user
    # which we use to cache results
    def get_grid_point(self):
        # Round longitude and latidude to nearest block-ish
        grid_longitude = self.longitude - self.longitude % (0.001)
        grid_latitude = self.latitude - self.latitude % (0.001)

        return {'longitude': grid_longitude, 'latitude': grid_latitude}
