from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . import models
from rest_framework import viewsets, permissions
from . import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.settings import api_settings

# Create your views here.
def index(request):
    return render(request,'front_end_crud/index.html')


def add_item(request):
    return render(request,'front_end_crud/add_item.html')
    

def save_item(request):
    if request.method== "POST":
        data=request.POST
        title=data.get("title")
        description=data.get("description")
        type_item=data.get("TypeItem")
        print(title,description,type_item)
        item=models.Item()
        item.title=data.get("title")
        item.description=data.get("description")
        item.type_item=data.get("TypeItem")
        item.price=data.get("price")
        item.save()

        print(models.Item.objects.all())
        return redirect(add_item)


def estoque(request):
    return render(request, 'front_end_crud/estoque.html')
def create_estoque(request):
    return render(request,'front_end_crud/add_estoque.html')




def save_estoque(request):
    if request.method=="POST":
        data=request.POST
        name=data.get("name")
        estoque=models.Estoque()
        estoque.name=name
        estoque.save()
        return redirect(create_estoque)


def view_itens(request):
    itens=models.Item.objects.all()
    context={'itens':itens}
    return render(request, 'front_end_crud/items.html', context)

def delete_item(request):
    if request.method=="POST":
        data=request.POST
        uuid=data.get('uuid')
        status=models.Item.objects.get(uuid=uuid).delete()
        if status=='1':
            pass


class EstoqueViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    queryset = models.Estoque.objects.all()
    serializer_class = serializers.EstoqueSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]