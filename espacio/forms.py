from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .validators import validate_dni, validate_cel, validate_tel, validate_str, validate_str

class UsuarioForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True, label='Numero de Usuario (DNI):', validators=[validate_dni])
	first_name = forms.CharField(max_length=30, required=False, label='Nombre:', validators=[validate_str])
	last_name = forms.CharField(max_length=30, required=False, label='Apellido:', validators=[validate_str])
	email = forms.EmailField(max_length=254)
	password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña:")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Contraseña (confirmación):")
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2', )

class AutenticacionForm(AuthenticationForm,):
	username=forms.CharField(max_length=30, required=True, label='Numero de Usuario (DNI):', validators=[validate_dni])
	password=forms.CharField(widget=forms.PasswordInput, label="Contraseña:")
	class Meta:
		model=User
		fields=('username', 'password')