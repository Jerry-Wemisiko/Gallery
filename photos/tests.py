from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTest(TestCase):
    def setUp(self):
        self.nairobi = Location(location = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
