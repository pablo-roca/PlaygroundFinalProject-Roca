from django import forms
from .models import Articulo, Cliente, Vendedor

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
    

class ArticuloFormulario(forms.ModelForm):
    class Meta:
        model = Articulo
        fields ='__all__'
        

class VendedorFormulario(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields  ='__all__'
        
class ClienteSearchForm(forms.Form):
    nombre = forms.CharField(required=False)