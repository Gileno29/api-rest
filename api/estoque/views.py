from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

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
        return redirect('add_item')

def view_itens(request):
    pass