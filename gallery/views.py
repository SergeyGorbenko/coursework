from django.shortcuts import render
from gallery.models import *


# Create your views here.


def home(request):
    gallerys = Gallery_unit.objects.all()
    photos = []
    for g in gallerys:
        photos += [Photo.objects.filter(gallery=g).first()]
    context = {'gallerys': gallerys, 'photos': photos}
    return render(request, 'index.html', context=context)


def gallery(request, gallery):
    g = Gallery_unit.objects.get(link=gallery)
    photos = Photo.objects.filter(gallery=g).all()
    context = {'gallery': g, 'photos': photos}
    return render(request, 'collection.html', context=context)
