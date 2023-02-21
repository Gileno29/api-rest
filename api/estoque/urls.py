from django.contrib import admin
from django.urls import path, include
from . import  views
from rest_framework.routers import DefaultRouter
from .views import EstoqueViewSet


app_name='estoque'

router = DefaultRouter(trailing_slash=False)
router.register(r'api', EstoqueViewSet)

urlpatterns = [

    path('', views.index, name='index'),
    path('additem', views.add_item, name="additem"),
    path('saveitem', views.save_item, name="saveitem"),
    path('addestoque', views.create_estoque, name="addestoque"),
    path('estoque', views.estoque, name='estoque'),
    path('viewitems', views.view_itens, name='viewitems'),
]