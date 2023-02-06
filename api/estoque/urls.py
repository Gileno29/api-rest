from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [

    path('', views.index, name='index'),
    path('additem', views.add_item, name="additem"),
    path('saveitem', views.save_item, name="saveitem")
]