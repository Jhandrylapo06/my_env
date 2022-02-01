from django.urls import path
from erp.views import primeravista,segundavista
urlpatterns = [
    
    path('vista1/',primeravista),
    path('vista2/',segundavista),
]