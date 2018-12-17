from django.urls import path, include
from . import views

urlpatterns = [
    path('gallerys/', views.home, name='home'),
    path('gallerys/<str:gallery>/', views.gallery, name='gallery'),
    path('gallerys/<str:gallery>/photos/', views.photos, name='photos'),
]
