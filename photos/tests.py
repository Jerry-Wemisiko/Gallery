from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.

class ImageTest(TestCase):
   
    def setUp(self):
        self.funny = Image(name ='Jerry', description = 'party mode',location = 'New York',category = 'Fun')

    def test_instance(self):
        self.assertTrue(isinstance(self.funny,Image))

    def test_save_method(self):
        self.funny.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    
