from django.shortcuts import render, get_object_or_404
from .models import Masa, Pizza, Ingrediente, Direccion
from .forms import crearPizzaForm, CommentForm
from django.http import  HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def homepage(request):
    masas = Masa.objects.all()
    ingredientes = Ingrediente.objects.all()
    context = {'masas':masas, 'ingredientes':ingredientes}
    return render(request, 'home.html', context)

def masaPage(request, pk):
    masa = get_object_or_404(Masa, pk = pk)
    pizzas = masa.pizza_set.all()
    comments = masa.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.masa = masa
            new_comment.save()
    else:
        comment_form = CommentForm()

    
    context = {'masa':masa, 'pizzas':pizzas, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form}
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
    
    if request.method == 'POST':
        pizzaForm = crearPizzaForm(data=request.POST)
        if pizzaForm.is_valid():
            print(11)
            newPizza = pizzaForm.save(commit=False)
            newPizza.save()
            url = reverse('home')
            return HttpResponseRedirect(url)
    else:
        pizzaForm = crearPizzaForm()

    context = {'ingredientes':ingredientes, 'masas':masas, 'form' : pizzaForm, 'newPizza':newPizza}
    
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



