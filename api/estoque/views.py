from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'front_end_crud/index.html')


def addItem(request):
    pass

def viewItens(request):
    pass