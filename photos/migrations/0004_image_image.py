# Generated by Django 3.2.7 on 2021-09-06 09:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_image_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(default='Pic', max_length=255, verbose_name='image'),
        ),
    ]
