from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30) #texto max 30 caracteres
    direccion=models.CharField(max_length=50, verbose_name="La dirección") #texto max 50 caracteres
    email=models.EmailField()
    tfno=models.CharField(max_length=7) #texto max 7 caracteres

    def __str__ (self):
        return "el nombre es %s" % (self.nombre)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30) #texto max 30 caracteres
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
