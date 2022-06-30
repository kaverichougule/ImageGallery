from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('addimages/',views.addimages,name='addimages'),
    path('photo/',views.photo,name='photo'),
    path('about/',views.about,name='about')
] 
