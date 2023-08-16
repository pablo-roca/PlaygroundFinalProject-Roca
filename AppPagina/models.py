from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    precio = models.FloatField()
    
    def __str__(self):
        return self.nombre

    
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.CharField(max_length=10)
    email = models.EmailField(default='modelo@example.com')

class Vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.CharField(max_length=10)
    num_vendedor = models.IntegerField()
    
