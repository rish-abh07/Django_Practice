from django.contrib import admin
from django.urls import path
from hoe import views

urlpatterns = [
    path("", views.index,name='hoe'),
    path("about", views.aboutus, name='about'),
    path("contactus",views.contact,name='contact')
    
]