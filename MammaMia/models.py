from django.db import models
from django.urls import reverse

# Create your models here.


class Masa(models.Model):
    nameMa = models.CharField(max_length = 255)
    image = models.ImageField(upload_to ='media')
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
    image = models.ImageField(upload_to = 'media')
    masa = models.ForeignKey(Masa, on_delete = models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)

    #ir desde una pizza a hacer pedido

class nuevaPizza(models.Model):
    nombre = models.CharField(max_length = 255)
    masa = models.ForeignKey(Masa, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)







