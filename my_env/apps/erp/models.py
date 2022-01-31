from django.db import models
from datetime import datetime

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=150) 
    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['id']

class Categoria(models.Model):
    nombre = models.CharField(max_length=150) 
    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['id']

class Empleado(models.Model):
    categoria = models.ManyToManyField(Categoria) 
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    nombres = models.CharField(max_length=150)
    cedula = models.CharField(max_length=10 , unique=True)
    fechaRegistro = models.DateField(default=datetime.now)
    edad = models.PositiveIntegerField(default=0)
    genero = models.CharField(max_length=50)
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    avatar = models.ImageField(null=True, blank = True)
    estado = models.BooleanField(default=True) 

    def __str__(self):
        return self.nombres

    class Meta:
        ordering = ['id']