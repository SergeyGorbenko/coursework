from django.shortcuts import render
from gallery.models import *
from gallery.forms import *


def home(request):
    if request.method == 'POST':
        form = CreateGallery(request.POST)
        if form.is_valid():
            gallery = Gallery_unit(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
            gallery.save()
    elif request.GET.get("gallery_name"):
        gallery = Gallery_unit.objects.get(link=request.GET.get("gallery_name"))
        gallery.delete()
    gallerys = Gallery_unit.objects.all()
    photos = []
    for g in gallerys:
        photos += [Photo.objects.filter(gallery=g).first()]
    context = {'gallerys': gallerys, 'photos': photos, 'form': CreateGallery()}
    return render(request, 'index.html', context=context)


def gallery(request, gallery):
    g = Gallery_unit.objects.get(link=gallery)

    if request.method == 'POST':
        form = LoadPhoto(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            photo = Photo(name=form.cleaned_data['photo'].name, photo=form.cleaned_data['photo'], gallery=g)
            photo.save()

    elif request.GET.get("photo_name"):
        photo = Photo.objects.get(link=request.GET.get("photo_name"))
        photo.delete()

    photos = Photo.objects.filter(gallery=g).all()
    context = {'gallery': g, 'photos': photos, 'form': LoadPhoto()}
    return render(request, 'collection.html', context=context)


def photos(request, gallery):
    g = Gallery_unit.objects.get(link=gallery)
    photos = Photo.objects.filter(gallery=g).all()
    context = {'photos': photos}
    return render(request, 'collection.html', context=context)
