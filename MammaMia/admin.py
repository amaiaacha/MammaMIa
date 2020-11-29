from django.contrib import admin
from .models import Masa, Ingrediente, Pizza, Direccion, nuevaPizza

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Masa)
admin.site.register(Ingrediente)
admin.site.register(Direccion)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'masa', 'ingredientes')
    search_fields = ('nombre', 'masa', 'ingredientes')
    actions = ['crear_pizza']

    def crear_pizza(self, request, queryset):
        queryset.update(active=True)