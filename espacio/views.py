from django.contrib import messages
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from .forms import UsuarioForm

def home(request):
    return render(request, 'home.html')


def registrarUsuario(request, tipo):
	if request.method=='POST':
		a=tipo
		form = UsuarioForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			if a=='Staff':
				if request.user.is_superuser:
					instance.is_staff=True
			instance.save()
			return redirect('home', )
	else:
		form = UsuarioForm()
	return render(request, 'usuarios/registro.html', {'form':form})


def loginUsuario(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('home')
	else:
		form = AuthenticationForm()
	return render(request, 'usuarios/login.html', {'form':form}) 


def logoutUsuario(request):
	if request.method == "POST":
		logout(request)
		return redirect('home')

def passwordUsuario(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Your password was successfully updated!')
			return redirect('home')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'usuarios/password.html', {'form': form})