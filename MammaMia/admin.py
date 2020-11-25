from django.contrib import admin
from .models import Masa, Ingrediente, Pizza, Direccion

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Masa)
admin.site.register(Ingrediente)
admin.site.register(Direccion)