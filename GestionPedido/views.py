from django.shortcuts import render
from django.http import HttpResponse 
from GestionPedido import models
# Create your views here.


def busqueda_productos(request):
    
    return render(request, "busqueda_productos.hmtl")

def buscar(request):
    if request.GET["prd"]:

       # mensaje="Articulo buscado: %r" %request.GET["prd"]
       producto=request.GET["prd"]

       articulos=models.Articulos.objects.filter(nombre__icontains=producto)

       return render(request,"resultados_busqueda.html",{"articulos":articulos, "query":producto})

    else:
        mensaje="no has introducido nada"
    return HttpResponse(mensaje)