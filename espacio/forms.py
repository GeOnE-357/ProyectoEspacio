from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class UsuarioForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True, label='Numero de Usuario (DNI):')
	first_name = forms.CharField(max_length=30, required=False, label='Nombre:')
	last_name = forms.CharField(max_length=30, required=False, label='Apellido:')
	email = forms.EmailField(max_length=254)
	password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña:")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Contraseña (confirmación):")
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2', )
