from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('cliente/', views.cliente, name='cliente'),
    path('vendedor/', views.vendedor, name='vendedor'),
    path('articulos/',views.articulos, name='articulos'),
    path('buscarCliente/',views.buscarCliente, name='buscarCliente')
    
    
]