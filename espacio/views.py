from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UsuarioForm

def home(request):
    return render(request, 'home.html')

def registrarUsuario(request):
	if request.method=='POST':
		form = UsuarioForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			if request.user.is_superuser:
				instance.is_staff = True
			instance.save()
			return redirect('home')
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