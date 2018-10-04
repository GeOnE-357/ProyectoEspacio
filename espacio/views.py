from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def home(request):
    return render(request, 'home.html')

def registrarUsuario(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()
			return redirect('home')
	else:
		form = UserCreationForm()
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