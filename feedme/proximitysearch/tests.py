from django.test import TestCase
from proximitysearch.models import FoodFinderInfo

class NearbyFoodFacilityTestCase(TestCase):
    def setUp(self):
        FoodFinderInfo.objects.create(name = "Testco", address="1770 Pacific", description="Imaginary food stuffs", longitude="37.794656", latitude="-122.424326")

    def test_get_distances(self):
        testco = FoodFinderInfo.objects.get(name="lion")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
