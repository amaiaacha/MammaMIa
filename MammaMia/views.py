from django.shortcuts import render, get_object_or_404
from .models import Masa, Pizza, Ingrediente, nuevaPizza
from .forms import crearPizzaForm


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

def crearPizza(request):
    masas = Masa.objects.all()
    ingredientes = Ingrediente.objects.all()
    newPizza = None
    if(request.method == 'POST'):
        form = crearPizzaForm(request.POST)
        if form.is_valid():
            newPizza = form.save(commit = False)
            newPizza.post = posts
            newPizza = form.save()
    else:
       form = crearPizzaForm()
    context = {'ingredientes':ingredientes, 'masas':masas, 'form' : form}
    
    return render(request, 'crearPizza.html', context)



