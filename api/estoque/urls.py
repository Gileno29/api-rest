from django.contrib import admin
from django.urls import path, include
from . import  views



urlpatterns = [

    path('', views.index, name='index'),
    path('additem', views.add_item, name="additem"),
    path('saveitem', views.save_item, name="saveitem"),
    path('addestoque', views.create_estoque, name="addestoque"),
    path('saveestoque', views.save_estoque, name="saveestoque"),
    path('estoque', views.estoque, name='estoque'),
    path('viewitems', views.view_itens, name='viewitems'),
]