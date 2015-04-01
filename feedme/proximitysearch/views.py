from proximitysearch.src.locationController import LocationController
from proximitysearch.src.locationValidator import LocationValidator

from proximitysearch.serializers import FoodFacilitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NearbyFoodFacilityList(APIView):
    """
    https://github.com/oahayder/feedme
    """
    def get(self, request, longitude, latitude):

        validate = LocationValidator.validate_coordinates(longitude,latitude)
        if (not validate):
            return Response("Invalid longitude and/or latitude params", status=status.HTTP_400_BAD_REQUEST)

        try:
            count = int(request.GET.get('count'))
        except (TypeError, ValueError) as e:
            # TODO Log error
            count = 1

        sorted_proximitysearch_list = LocationController.get_nearby_food_facilities(float(longitude), float(latitude))
        serializer = FoodFacilitySerializer(sorted_proximitysearch_list[0:count], many=True)

        return Response(serializer.data)

