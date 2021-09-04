from photos.models import Category, Location,Image
from django.contrib import admin

# Register your models here.
admin.site.register(Image)
admin.site.register(Location)
admin.register(Category)
