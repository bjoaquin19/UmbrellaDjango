from django import forms
from django.forms import ModelForm, Form #fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Categoria, Producto, Bodega, Perfil

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(),
            'imagen': forms.FileInput(attrs = {'class': 'd-none'}) #
            }
        labels = {
            'nombre': 'Nombre',
            'descuento_subscriptor': 'Subscriptor(%)',
            'descuento_Oferta': 'Oferta(%)'
        }

class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label='Cuenta')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    class Meta:
        fields = ['username', 'password']

class RegistroForm():
    class Meta:
        model = Perfil
        fields = '__all__'

class BodegaForm(Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría')
    producto = forms.ModelChoiceField(queryset=Producto.objects.none(), label='Producto')
    cantidad = forms.IntegerField(label='Cantidad')
    class Meta:
        fields = '__all__'

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {'password1': forms.PasswordInput(),
                   'password2': forms.PasswordInput()}
        
        labels = {'username': 'Nombre de usuario',
                  'first_name': 'Nombre',
                  'last_name': 'Apellido',
                  'email': 'Correo',
                  'password1': 'Contraseña',
                  'password2': 'Repetir Contraseña'
                  }

class RegistroPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['rut', 'direccion', 'subscrito', 'imagen']
        exclude = ['tipo_usuario']
        widgets = {'direccion': forms.Textarea(),
                   'imagen': forms.FileInput()
                   }

class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {'password': forms.PasswordInput()}
        labels = {
            'email': 'E-mail'
        }

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['tipo_usuario', 'rut', 'direccion', 'subscrito', 'imagen']
        widgets = {
            'direccion': forms.Textarea(),
            'imagen': forms.FileInput(),
        }
        labels = {
            'tipo_usuario': 'Tipo de Usuario',
            'rut': 'Rut',
            'direccion': 'Dirección',
            'subscrito': 'Subscrito',
            'imagen': 'Imagen de Perfil',
        }


