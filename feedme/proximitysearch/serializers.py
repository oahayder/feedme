from proximitysearch.models import FoodFinderInfo

from rest_framework import serializers

class FoodFinderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodFinderInfo
        fields = ('name', 'address', 'description', 'scheduleLink', 'distance')
