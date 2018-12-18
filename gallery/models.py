from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


# Create your models here.

class Gallery_unit(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=40, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.link = "_".join(self.name.lower().split())
        super().save()

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=40, unique=True)
    create = models.DateTimeField(auto_now_add=True, blank=True)
    photo = models.ImageField(upload_to='gallery_photos')
    gallery = models.ForeignKey('Gallery_unit', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
