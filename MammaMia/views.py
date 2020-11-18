from django.shortcuts import render, get_object_or_404
from .models import Masa, Pizza


# Create your views here.
def homepage(request):
    masas = Masa.objects.all()
    context = {'masas':masas}
    return render(request, 'home.html', context)

def masaPage(request, pk):
    masas = get_object_or_404(Masa, pk = pk)
    pizzas = Pizza.objects.filter(pk=pk) 
    ingredientes = Ingrediente.objects.filter(pk=pk)
    context = {'masas':masas, 'pizzas':pizzas, 'ingredientes':ingredientes}

    return render(request, 'masaPage.html', context)



