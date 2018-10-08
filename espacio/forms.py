from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsuarioForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True, label='Nombre de Usuario:', help_text='Parametro obligatorio. Únicamente letras, dígitos y @/./+/-/_')
	first_name = forms.CharField(max_length=30, required=False, label='Nombre:')
	last_name = forms.CharField(max_length=30, required=False, label='Apellido:')
	email = forms.EmailField(max_length=254, help_text='Parametro obligatorio. Introdusca un mail valido.')
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )