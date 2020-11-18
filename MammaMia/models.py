from django.db import models
from django.urls import reverse

# Create your models here.


class Masa(models.Model):
    nameMa = models.CharField(max_length = 255)
    image = models.ImageField(upload_to ='media')
    
    def getMasa(self):
        return reverse('masaPage', args=[self.pk])

class Ingrediente(models.Model):
    nameIn = models.CharField(max_length = 500)

class Pizza(models.Model):
    namePi = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'media')
    masa = models.ForeignKey(Masa, on_delete = models.CASCADE, default = 27)
    ingredientes = models.ManyToManyField(Ingrediente)





