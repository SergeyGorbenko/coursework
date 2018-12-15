from django.urls import path, include
from . import views

urlpatterns = [
    path('gallerys/', views.home, name='home'),
    path('gallery/<str:gallery>/', views.gallery, name='gallery'),
]
