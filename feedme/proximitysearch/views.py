from django.shortcuts import render
from proximitysearch.models import FoodFinderInfo

from proximitysearch.serializers import FoodFinderInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class FoodFinderList(APIView):
    """
    Where are the nearest food trucks? I'm hungry
    """
    def get(self, request, latitude, longitude, count=5):
        # TODO Get the grid point

        # Does this coordinate live in the cache?

        # If not, we'll have to build it
        # TODO STATUS=APPROVED
        all_facilities = FoodFinderInfo.objects.all()

        proximitysearch_list = []
        for proximitysearch in all_facilities:
            # Get distance
            distance = proximitysearch.get_distance_from(float(longitude), float(latitude))
            proximitysearch.set_distance(round(distance,1))
            proximitysearch_list.append(proximitysearch)

        # Sort it
        sorted_proximitysearch_list = sorted(proximitysearch_list, key=lambda item: item.distance)

        # TODO Store in cache?

        serializer = FoodFinderInfoSerializer(sorted_proximitysearch_list[0:count], many=True)
        return Response(serializer.data)

