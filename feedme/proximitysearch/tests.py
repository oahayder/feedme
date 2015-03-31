from django.test import TestCase
from proximitysearch.models import FoodFacility
from proximitysearch.src.locationController import LocationController
from proximitysearch.src.locationValidator import LocationValidator

class NearbyFoodFacilityTestCase(TestCase):
    def setUp(self):
        FoodFacility.objects.create(name = "Testco", address="1770 Pacific", description="Imaginary food stuffs", longitude="37.794656", latitude="-122.424326")

    def test_get_distances(self):
        testco = FoodFacility.objects.get(name="lion")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_invalid_input(self):
        self.assertEqual(LocationValidator.validate_coordinates(0,0), 1)
        self.assertEqual(LocationValidator.validate_coordinates(180,90), 1)
        self.assertEqual(LocationValidator.validate_coordinates(-180,-90), 1)
        self.assertEqual(LocationValidator.validate_coordinates(180,-90), 1)
        self.assertEqual(LocationValidator.validate_coordinates(-180,90), 1)
        self.assertEqual(LocationValidator.validate_coordinates(1000,0), 0)
        self.assertEqual(LocationValidator.validate_coordinates(0,-1000), 0)
        self.assertEqual(LocationValidator.validate_coordinates(-1000,0), 0)
        self.assertEqual(LocationValidator.validate_coordinates(0,10000), 0)
        self.assertEqual(LocationValidator.validate_coordinates("a",True), 0)
