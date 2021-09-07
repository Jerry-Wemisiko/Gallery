from photos.views import location
from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.

class LocationTest(TestCase):
    def setUp(self):
        self.kanairo = Location(location = 'Nairobi')
        self.kanairo.save_location()

    def tearDown(self):
        self.kanairo.delete_location()


    def test_update_location(self):
        location = Location.get_location_by_id(self.kanairo.id)
        location.update_location('Monaco')
        location = Location.get_location_by_id(self.kanairo.id)
        self.assertTrue(location.location == 'Monaco')


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

    
class CategoryTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.lifestyle = Category(category='Lifestyle')
        self.lifestyle.save_category()

    
    def tearDown(self):
        self.lifestyle.delete_category()
    
    def test_updating_category(self):
        category = Category.get_category_id(self.lifestyle.id)
        category.update_category('Tech')
        category = Category.get_category_id(self.lifestyle.id)
        self.assertTrue(category.category == 'Tech')
    
        
    
