from django.db import models

class FacilityInfo(models.Model):
    id = models.TextField()
    name = models.TextField()
    address = models.TextField()
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    scheduleLink = models.TextField()
    lastUpdatedTimestamp = models.DateField.auto_now

    def __unicode__(self):
        return self.name

