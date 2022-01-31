from re import template
from django.http import HttpResponse
from django.shortcuts import render 

# Create your views here.
def primeravista(request):
    return render(request,'templates/index.html') 
