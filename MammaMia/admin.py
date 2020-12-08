from django.contrib import admin
from .models import Masa, Ingrediente, Pizza, Direccion, Comment

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Masa)
admin.site.register(Ingrediente)
admin.site.register(Direccion)
admin.site.register(Comment)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('namePi', 'masa', 'ingredientes')
    search_fields = ('namePi', 'masa', 'ingredientes')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contenido', 'masa', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('nombre', 'contenido')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)