from django.db import models
from django.urls import reverse

# Create your models here.

class Masa(models.Model):
    nameMa = models.CharField(max_length = 255)
    image = models.ImageField(upload_to ='media')
    descripcion = models.CharField(max_length = 255)
    pizzas = models.ManyToManyField(Pizza, on_delete = models.CASCADE)

    def getMasa(self):
        return reverse('masaPage', args=[self.pk])
        
class Ingrediente(models.Model):
    nameIn = models.CharField(max_length = 500)
    pizzas = models.ManyToManyField(Pizza, on_delete = models.CASCADE)

class Pizza(models.Model):
    namePi = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'media')
    masas = models.ManyToManyField(Masa, on_delete = models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente, on_delete = models.CASCADE)




