from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.location
    
    def save_location(self):
        return self.save()

    def delete_location(self):
        return self.delete()

    def update_location(self):
        return self.update()

    @classmethod
    def get_location_by_id(self,id):
        location = Location.objects.get(id=id)
        return location

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.category


    def save_category(self):
        return self.save()

    def delete_category(self):
        return self.delete()
    
    @classmethod
    def get_category_id(cls,id):
      category= Category.objects.get(id=id)
      return category
    

    class Meta:
        verbose_name_plural = 'Categories'


class Image(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE ,blank=True)
    image = CloudinaryField('images')


    def __str__(self) -> str:
        return self.name

    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()
    
    def update_image(self):
        self.update()
        
    @classmethod
    def search_image_category(cls,search_image):
        images = cls.object.filter(category__icontains = search_image)
        return images

    @classmethod
    def get_images(cls):
        all_images = Image.objects.all()
        return all_images

    @classmethod
    def get_image_by_id(self,id):
        image = Image.objects.get(id=id)
        return image

    

    

    

    

    
