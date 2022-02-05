from django.urls import path
from erp.views import primeravista,segundavista

app_name = 'erp'
urlpatterns = [
    
    path('vista1/',primeravista, name='vista1' ),
    path('vista2/',segundavista, name='vista2' ),
]