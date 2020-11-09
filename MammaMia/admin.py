from django.contrib import admin
from .models import Masa, Ingrediente, Pizza

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Masa)
admin.site.register(Ingrediente)