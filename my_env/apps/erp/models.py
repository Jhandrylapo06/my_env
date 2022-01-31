from urllib.parse import _NetlocResultMixinBytes
from django.db import models
from datetime import datetime
from erp.Choices import gender_choices

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=150,unique=True) 
    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['id']

class Producto(models.Model):
    nombre = models.CharField(max_length=150,unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    imagen = models.ImageField(null=True,blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['id']

class Cliente(models.Model):
    
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    cedula = models.CharField(max_length=10 , unique=True)
    fechaNacimiento = models.DateField(default=datetime.now)
    direccion = models.CharField(max_length=150, null=True, blank= True)
    genero = models.CharField(max_length=10, choices= gender_choices,default='Masculino')


    def __str__(self):
        return self.nombres

    class Meta:
        ordering = ['id']

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaventa = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)


    def __str__(self):
        return self.cliente.nombres

    class Meta:
        ordering = ['id']


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0) 
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)


    def __str__(self):
        return self.producto.nombre

    class Meta:
        ordering = ['id']