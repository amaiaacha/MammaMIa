from django.db import models
from django.urls import reverse

# Create your models here.


class Masa(models.Model):
    nameMa = models.CharField(max_length = 255)
    image = models.ImageField(upload_to ='masas')
    descrip = models.CharField(max_length = 500)
    
    def getMasa(self):
        return reverse('masaPage', args=[self.pk])
    
    def __str__(self):
        return self.nameMa

class Ingrediente(models.Model):
    nameIn = models.CharField(max_length = 500)
    calorias = models.CharField(max_length = 4)
    descrip = models.CharField(max_length = 355)

    def __str__(self):
        return self.nameIn

    def getIngrediente(self):
        return reverse('ingredPage', args=[self.pk])


class Pizza(models.Model):
    namePi = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'pizzas', null=True)
    masa = models.ForeignKey(Masa, on_delete = models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.namePi

class nuevaPizza(models.Model):
    nombre = models.CharField(max_length = 255)
    masa = models.ForeignKey(Masa, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)

class Direccion(models.Model):
    direccion = models.CharField(max_length=600)
    numeroTelf = models.IntegerField(blank=True)
    image = models.ImageField(upload_to = 'tiendas')

    def __str__(self):
        return self.direccion





