from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('masaPage/<int:pk>', views.masaPage, name = 'masaPage'),
    path('crearPizza/', views.crearPizza, name = 'crearPizza'),
]