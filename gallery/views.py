from django.shortcuts import render
from gallery.models import *
from gallery.forms import *


def home(request):
    if request.method == 'POST':
        pass
    else:
        gallerys = Gallery_unit.objects.all()
        photos = []
        for g in gallerys:
            photos += [Photo.objects.filter(gallery=g).first()]
        context = {'gallerys': gallerys, 'photos': photos, 'form': CreateGallery()}
        return render(request, 'index.html', context=context)


def gallery(request, gallery):
    if request.method == 'POST':
        pass
    else:
        g = Gallery_unit.objects.get(link=gallery)
        photos = Photo.objects.filter(gallery=g).all()
        context = {'gallery': g, 'photos': photos, 'form': LoadPhoto()}
        return render(request, 'collection.html', context=context)
