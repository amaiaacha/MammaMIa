from django.shortcuts import render, get_object_or_404
from .models import Masa, Pizza, Ingrediente, nuevaPizza, Direccion
from .forms import crearPizzaForm


# Create your views here.
def homepage(request):
    masas = Masa.objects.all()
    ingredientes = Ingrediente.objects.all()
    context = {'masas':masas, 'ingredientes':ingredientes}
    return render(request, 'home.html', context)

def masaPage(request, pk):
    masas = get_object_or_404(Masa, pk = pk)
    #hay que cambiar
    pizzas = masas.pizza_set.all()
    #ingredientes = Ingrediente.objects.filter(pk=pk)
    context = {'masas':masas, 'pizzas':pizzas}

    return render(request, 'masaPage.html', context)

def ingredPage(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk = pk)
    pizzas = ingrediente.pizza_set.all()
    context = {'ingrediente':ingrediente, 'pizzas':pizzas}

    return render(request, 'ingredPage.html', context)

def crearPizza(request):
    masas = Masa.objects.all()
    ingredientes = Ingrediente.objects.all()
    newPizza = None
    if(request.method == 'POST'):
        form = crearPizzaForm(request.POST)
        if form.is_valid():
            newPizza = form.save(commit = False)
            newPizza = form.save()
    else:
       form = crearPizzaForm()
       
    context = {'ingredientes':ingredientes, 'masas':masas, 'form' : form, 'newPizza':newPizza}
    
    return render(request, 'crearPizza.html', context)



def pizzas(request):
    pizza = Pizza.objects.all()
    context  = {'pizza':pizza}
    
    return render(request, 'pizzas.html', context)

def who(request):
    direccion = Direccion.objects.all()
    numeroTelf = Direccion.objects.all()
    context = {'direccion':direccion, 'numeroTelf': numeroTelf}
    
    return render(request, 'who.html', context)



