__author__ = 'oahayder'

class LocationValidator(object):
    @staticmethod
    def validate_coordinates(longitude, latitude):
        try:
            longitude = float(longitude)
            latitude = float(latitude)
        except (TypeError, ValueError):
            # TODO Log error
            # TODO try and use the users previously requested location
            # TODO Use custom exception
            return 0


        if (longitude>180 or longitude<-180 or latitude>90 or latitude<-90):
            return 0

        return 1
