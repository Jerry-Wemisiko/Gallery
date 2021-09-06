from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.location


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'

class Image(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE ,blank= True)



    def __str__(self) -> str:
        return self.name

    def save_image(self):
        self.save()

    class Meta:
        ordering = ['name']

    def delete_image(self):
        self.delete()

    

    

    

    
