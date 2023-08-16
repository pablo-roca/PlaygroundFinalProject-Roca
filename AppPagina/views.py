from django.shortcuts import render, redirect
from django.template import Template,Context,loader
from django.http import HttpResponse

from .models import Cliente,Articulo, Vendedor
from .forms import ClienteFormulario, ArticuloFormulario, VendedorFormulario, ClienteSearchForm

# Create your views here.


def cliente(request):
    if request.method == 'POST':
        cliente_formulario = ClienteFormulario(request.POST)
        
        if cliente_formulario.is_valid:
            cliente_formulario.save()
            
            return redirect('/AppPagina/')
    else:
        cliente_formulario = ClienteFormulario()
    
        return render(request, 'AppPagina/cliente.html',{"cliente_formulario": cliente_formulario})
    

def inicio(request):
    return render(request,'AppPagina/inicio.html')

def vendedor(request):
    if request.method == 'POST':
        vendedor_formulario = VendedorFormulario(request.POST)
        
        if vendedor_formulario.is_valid:
            vendedor_formulario.save()
            
            return redirect('/AppPagina/')
    else:
        vendedor_formulario = VendedorFormulario()
    
    
    return render(request,'AppPagina/vendedor.html',{"vendedor_formulario":vendedor_formulario})

def articulos(request):
    if request.method == 'POST':
        articulo_formulario = ArticuloFormulario(request.POST)
        
        if articulo_formulario.is_valid():
            articulo_formulario.save()       
            return redirect('/AppPagina/')
    else:
        articulo_formulario = ArticuloFormulario()
    
    return render(request, 'AppPagina/articulos.html',{"articulo_formulario": articulo_formulario})
    

def buscarCliente(request):
    clientes = []
    form = ClienteSearchForm(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if nombre:
            clientes= Cliente.objects.filter(nombre__icontains=nombre)

    return render(request, 'AppPagina/buscarCliente.html', {'form': form, 'clientes': clientes})