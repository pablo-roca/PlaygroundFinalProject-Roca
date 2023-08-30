from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name='inicio'),
    #path urls buscar de clases
    path('buscarCliente/',views.buscarCliente, name='buscarCliente'),
    path('buscarArticulo/',views.buscarArticulo, name='buscarArticulo'),
    
    #path urls de articulo
    path('articulo/nuevo/',views.ArticuloCreateView.as_view(), name='articulo'),
    path('articulo/lista/', views.ArticuloListView.as_view(), name = 'articulo_list'),
    path('articulo/<pk>/borrar/', views.ArticuloDeleteView.as_view(), name='ArticuloDeleteView'),
    path('articulo/<pk>/', views.ArticuloDetailView.as_view(), name='ArticuloDetailView'),
    path('articulo/<pk>/editar/', views.ArticuloUpdateView.as_view(), name='ArticuloUpdateView'),
    
    #path urls de vendedor
    path('vendedor/lista/', views.VendedorListView.as_view(), name = 'vendedor_list'),
    path('vendedor/nuevo/', views.VendedorCreateView.as_view(), name='vendedor'),
    path('vendedor/<pk>/borrar/', views.VendedorDeleteView.as_view(), name='VendedorDeleteView'),
    path('vendedor/<pk>/', views.VendedorDetailView.as_view(), name='VendedorDetailView'),
    path('vendedor/<pk>/editar/', views.VendedorUpdateView.as_view(), name='VendedorUpdateView'),
    
    #path urls de cliente
    path('cliente/nuevo/', views.ClienteCreateView.as_view(), name='cliente'),
    path('cliente/lista/', views.ClienteListView.as_view(), name = 'cliente_list'),
    path('cliente/<pk>/borrar/', views.ClienteDeleteView.as_view(), name='ClienteDeleteView'),
    path('cliente/<pk>/editar/', views.ClienteUpdateView.as_view(), name='ClienteUpdateView'),
    path('cliente/<pk>/', views.ClienteDetailView.as_view(), name='ClienteDetailView'),
    
    
    
]