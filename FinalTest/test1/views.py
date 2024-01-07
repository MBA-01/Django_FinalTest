from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

# def index(response,id):
#     return HttpResponse("<h1>%s</h1> <br> <br> <h4>%s</h4>" % (ToDoList.objects.get(id=id),Item.objects.get(id=id)))

# or we can do it in this way 

def index(response,id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=id)
    return HttpResponse("Message : <h1>%s</h1> <br><br> <h3>%s</h3>" % (ls.name,item.text))