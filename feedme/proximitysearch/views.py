from django.shortcuts import render
from proximitysearch.models import FoodFinderInfo

from proximitysearch.serializers import FoodFinderInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import logging
logging.basicConfig()

class FoodFinderList(APIView):
    """
    https://github.com/oahayder/feedme
    """
    def get(self, request, longitude, latitude):
        try:
            longitude = float(longitude)
            latitude = float(latitude)
        except (TypeError, ValueError):
            # TODO Log error
            # TODO try and use the users previously requested location
            # TODO Use custom exception
            return Response("Invalid regLong and/or reqLat params", status=status.HTTP_400_BAD_REQUEST)

        try:
            count = int(request.GET.get('count'))
        except (TypeError, ValueError) as e:
            # TODO Log error
            count = 1

        # TODO Get this max qeury count from conf
        if (count>20):
            count=20

        longitude -= longitude % (0.0001)
        latitude -= latitude % (0.0001)

        # TODO get the results from cache if it exists

        # TODO Can we get APPROVED from a decode table via public API?
        all_facilities = FoodFinderInfo.objects.filter(status='APPROVED')

        proximitysearch_list = []
        for proximitysearch in all_facilities:
            distance = proximitysearch.get_distance_from(longitude, latitude)
            proximitysearch.set_distance(round(distance,2))
            proximitysearch_list.append(proximitysearch)

        sorted_proximitysearch_list = sorted(proximitysearch_list, key=lambda item: item.distance)

        # TODO Store in cache

        serializer = FoodFinderInfoSerializer(sorted_proximitysearch_list[0:count], many=True)
        return Response(serializer.data)

