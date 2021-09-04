from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)


class Category(models.Model):
    category = models.CharField(max_length=30)

class Image(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    
