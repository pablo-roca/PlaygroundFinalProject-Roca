from django import forms
from .models import Articulo, Cliente, Vendedor, Post
from django.contrib.auth.forms import UserCreationForm, UserModel

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

class ArticuloSearchForm(forms.Form):
    nombre = forms.CharField(required=False)
    
class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label = "Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget= forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']