import os

from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render

from coursework import settings
from gallery.models import *
from gallery.forms import *


def home(request):
    gallerys = Gallery_unit.objects.all()
    context = {'gallerys': gallerys, 'form': CreateGallery()}
    if request.method == 'POST':
        form = CreateGallery(request.POST)
        if form.is_valid():
            try:
                gallery = Gallery_unit(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
                gallery.save()
            except IntegrityError:
                context['error'] = 'Gallery exist'
    elif request.GET.get("gallery_name"):
        gallery = Gallery_unit.objects.get(link=request.GET.get("gallery_name"))
        gallery.delete()
    return render(request, 'index.html', context=context)


def gallery(request, gallery):
    g = Gallery_unit.objects.get(link=gallery)
    photos = Photo.objects.filter(gallery=g).all()
    context = {'gallery': g, 'photos': photos, 'form': LoadPhoto()}

    if request.method == 'POST':
        form = LoadPhoto(request.POST, request.FILES)
        if form.is_valid():
            try:
                photo = Photo(name=form.cleaned_data['photo'].name, photo=form.cleaned_data['photo'], gallery=g)
                photo.save()
            except IntegrityError:
                context['error'] = 'Photo exist'

    return render(request, 'collection.html', context=context)


def photos(request, gallery):
    if request.GET.get("photo_name"):
        photo = Photo.objects.filter(name=request.GET.get("photo_name")).first()
        photo.delete()
    g = Gallery_unit.objects.get(link=gallery)
    photos = Photo.objects.filter(gallery=g).all()
    context = {'photos': photos[1:], 'link': g.link, 'first_photo': photos[0]}
    return render(request, 'full_screen.html', context=context)


def first_page(request):
    return HttpResponseRedirect("/gallerys/")
