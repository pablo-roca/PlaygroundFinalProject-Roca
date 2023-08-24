from django.shortcuts import render, redirect
from django.template import Template,Context,loader
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente,Articulo, Vendedor
from .forms import ClienteFormulario, ArticuloFormulario, ArticuloSearchForm, ClienteSearchForm

# Create your views here.




def inicio(request):
    return render(request,'AppPagina/inicio.html')


def buscarCliente(request):
    clientes = []
    form = ClienteSearchForm(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if nombre:
            clientes= Cliente.objects.filter(nombre__icontains=nombre)

    return render(request, 'AppPagina/buscarCliente.html', {'form': form, 'clientes': clientes})

def buscarArticulo(request):
    articulos = []
    form = ArticuloSearchForm(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if nombre:
            articulos= Articulo.objects.filter(nombre__icontains=nombre)

    return render(request, 'AppPagina/buscarArticulo.html', {'form': form, 'articulos': articulos})

#cliente vistas
class ClienteListView(ListView):
    model = Cliente
    template_name = 'AppPagina/cliente_list.html'
    context_object_name = 'cliente'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'dni', 'email']
    template_name= 'AppPagina/cliente.html'
    success_url = reverse_lazy('AppPagina:cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'AppPagina/cliente_delete.html'
    success_url = reverse_lazy('AppPagina:cliente_list')
    
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'AppPagina/cliente_detalle.html'

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'dni', 'email']
    template_name ='AppPagina/cliente_update.html'
    success_url = reverse_lazy('AppPagina:cliente_list')
    
    

#vendedor vistas
class VendedorListView(ListView):
    model = Vendedor
    template_name ='AppPagina/vendedor_list.html'
    context_object_name = 'vendedor'

class VendedorCreateView(CreateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'dni', 'num_vendedor']
    template_name = 'AppPagina/vendedor.html'
    success_url = reverse_lazy('AppPagina:vendedor_list')

class VendedorDeleteView(DeleteView):
    model = Vendedor
    template_name = 'AppPagina/vendedor_delete.html'
    success_url = reverse_lazy('AppPagina:vendedor_list')

class VendedorDetailView(DetailView):
    model = Vendedor
    template_name = 'AppPagina/vendedor_detalle.html'


#articulos vistas
class ArticuloListView(ListView):
    model = Articulo
    template_name = 'AppPagina/articulo_list.html'
    context_object_name = 'articulo'

class ArticuloCreateView(CreateView):
    model = Articulo
    fields = ['nombre', 'marca', 'tipo', 'precio']
    template_name = 'AppPagina/articulos.html'
    success_url = reverse_lazy('AppPagina:articulo_list')
        
class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'AppPagina/articulo_delete.html'
    success_url = reverse_lazy('AppPagina:articulo_list')

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'AppPagina/articulo_detalle.html'


    
    
    