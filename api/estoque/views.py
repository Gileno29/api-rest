from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . import models

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

def view_itens(request):
    pass

def dele_item(request):
    if request.method=="POST":
        data=request.POST
        uuid=data.get('uuid')
        status=models.Item.objects.get(uuid=uuid).delete()
        if status=='1':
            
