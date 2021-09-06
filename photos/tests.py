from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.

class ImageTest(TestCase):
   
    def setUp(self):

        self.funny = Image(name ='Jerry', description = 'party mode',location = 'New York',category = 'Fun')
        self.funny.save_image()

        self.kanairo = Location(location= 'Kanairo')
        self.kanairo.save_location()

        self.lifestyle = Category(category = 'Lifestyle')
        self.lifestyle.save_category()

    

    def tearDown(self):
        self.funny.delete_image()
        self.kanairo.delete_location()
        self.lifestyle.delete_category()

    def test_get_images(self):
        images = Image.objects.get_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images = Image.get_image_by_id(self.funny.id)
        self.assertTrue(images == self.funny)

    def test_search_by_image_category(self):
        images = Image.search_image_category('Lifestyle')
        self.assertTrue(images == self.lifestyle)
        self.assertTrue(len(images)>0)

    

    
        
    
