from django.shortcuts import render, redirect
from django.template import Template,Context,loader
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente,Articulo, Vendedor, Post
from .forms import PostForm, ArticuloFormulario, ArticuloSearchForm, ClienteSearchForm, UserCreationFormCustom
#login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#login 
#--------------------------------------------------------------------------------------------------
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password= contrasenia)
            
            login(request, user)
            
            return render(request,'AppPagina/inicio.html',{"mensaje": f'Bienvenido {user.username}'} )
    
    else:
        form = AuthenticationForm()
        
    return render (request, 'AppPagina/login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
                        
            return render(request,'AppPagina/inicio.html',{"mensaje": "usuario creado" })
    
    else:
        form = UserCreationFormCustom()
        
    return render (request, 'AppPagina/registro.html', {'form': form})
    



#--------------------------------------------------------------------------------------------------
@login_required
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
#---------------------------------------------------------------------------------
class ClienteListView(ListView):
    model = Cliente
    template_name = 'AppPagina/cliente_list.html'
    context_object_name = 'cliente'

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'dni', 'email']
    template_name= 'AppPagina/cliente.html'
    success_url = reverse_lazy('AppPagina:cliente_list')

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'AppPagina/cliente_delete.html'
    success_url = reverse_lazy('AppPagina:cliente_list')
    
class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'AppPagina/cliente_detalle.html'

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'dni', 'email']
    template_name ='AppPagina/cliente_update.html'
    success_url = reverse_lazy('AppPagina:cliente_list')
    
    

#vendedor vistas
#---------------------------------------------------------------------------------
class VendedorListView(ListView):
    model = Vendedor
    template_name ='AppPagina/vendedor_list.html'
    context_object_name = 'vendedor'

class VendedorCreateView(LoginRequiredMixin, CreateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'dni', 'num_vendedor']
    template_name = 'AppPagina/vendedor.html'
    success_url = reverse_lazy('AppPagina:vendedor_list')

class VendedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendedor
    template_name = 'AppPagina/vendedor_delete.html'
    success_url = reverse_lazy('AppPagina:vendedor_list')

class VendedorDetailView(LoginRequiredMixin, DetailView):
    model = Vendedor
    template_name = 'AppPagina/vendedor_detalle.html'

class VendedorUpdateView(LoginRequiredMixin,UpdateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'dni', 'num_vendedor']
    template_name ='AppPagina/vendedor_update.html'
    success_url = reverse_lazy('AppPagina:vendedor_list')


#articulos vistas
#---------------------------------------------------------------------------------
class ArticuloListView(ListView):
    model = Articulo
    template_name = 'AppPagina/articulo_list.html'
    context_object_name = 'articulo'

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ['nombre', 'marca', 'tipo', 'precio']
    template_name = 'AppPagina/articulos.html'
    success_url = reverse_lazy('AppPagina:articulo_list')
        
class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = 'AppPagina/articulo_delete.html'
    success_url = reverse_lazy('AppPagina:articulo_list')

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'AppPagina/articulo_detalle.html'
    
class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ['nombre', 'marca', 'tipo', 'precio']
    template_name ='AppPagina/articulo_update.html'
    success_url = reverse_lazy('AppPagina:articulo_list')



#Post
#-------------------------------------------------------------------------------------------
class PostListView(ListView):
    model = Post
    template_name = 'AppPagina/post_list.html'
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'AppPagina/post_create.html'
    success_url = reverse_lazy('AppPagina:post_list')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'AppPagina/post_update.html'
    success_url = reverse_lazy('AppPAgina:post_list')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'AppPagina/post_delete.html'
    success_url = reverse_lazy('AppPagina:post_list')    
    
    