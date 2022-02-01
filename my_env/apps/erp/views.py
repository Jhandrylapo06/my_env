from re import template
from django.http import HttpResponse
from django.shortcuts import render

from erp.models import Categoria, Producto 

# Create your views here.
def primeravista(request):
    data = {
        'categorias' : Categoria.objects.all()
    }
    return render(request,'templates/index.html', data) 


def segundavista(request):
    data = {
        'productos' : Producto.objects.all()
    }
    return render(request,'templates/segundo.html', data) 