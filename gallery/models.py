from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


# Create your models here.

class Gallery_unit(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=10)


class Photo(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True, blank=True)
    photo = models.ImageField(upload_to='gallery_photos')
    gallery = models.ForeignKey('Gallery_unit', on_delete=models.CASCADE)
    tags = models.ForeignKey('Tag', on_delete=models.CASCADE)
