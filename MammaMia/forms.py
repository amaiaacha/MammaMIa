from django import forms
from .models import Pizza, Comment

class crearPizzaForm(forms.ModelForm):
    class Meta:
      model = Pizza
      fields = ['namePi', 'masa', 'ingredientes']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nombre', 'contenido')