from proximitysearch.models import FoodFacility

from rest_framework import serializers

class FoodFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodFacility
        fields = ('name', 'address', 'description', 'scheduleLink', 'distance')
