from django import forms
from .models import nuevaPizza

class crearPizzaForm(forms.ModelForm):
    class Meta:
      model = nuevaPizza
      fields = ['nombre', 'masa', 'ingredientes']
