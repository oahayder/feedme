from proximitysearch.models import FoodFacility
from math import radians, cos, sin, asin, sqrt

__author__ = 'oahayder'

class LocationController(object):

    def get_cacheable_longitude(longitude):
        # TODO read this from conf
        longitude -= longitude % (0.0001)
        return longitude

    @staticmethod
    def get_cacheable_latitude(latitude):
        # TODO Read this from conf
        latitude -= latitude % (0.0001)
        return latitude

    @staticmethod
    def get_distance_between(lon1, lat1, lon2, lat2):

        # In miles
        # TODO read the desired metric setting from a User config
        earth_radius = 3963.1676

        # Uses the Haversine Formula (http://en.wikipedia.org/wiki/Haversine_formula)
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))

        distance = earth_radius * c

        return distance

    @staticmethod
    def get_nearby_food_facilities(longitude, latitude):


        # TODO Use custon redis cache to store results and grab them here
        # TODO Can we get APPROVED from a decode table via public API? Are approved the only open ones?
        approved_facilities = LocationController.get_approved_food_facilities()

        facilitysearch_list = []
        for facility in approved_facilities:
            distance = LocationController.get_distance_between(facility.longitude, facility.latitude, longitude, latitude)

            # TODO Should we not be rounding here and leave it up to the FE?
            facility.set_distance(round(distance,2))
            facilitysearch_list.append(facility)

        sorted_facilitysearch_list = sorted(facilitysearch_list, key=lambda item: item.distance)

        return sorted_facilitysearch_list

    @staticmethod
    def get_approved_food_facilities():
        approved_facilities = FoodFacility.objects.filter(status='APPROVED')
        return approved_facilities
