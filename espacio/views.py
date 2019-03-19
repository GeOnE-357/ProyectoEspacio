from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm

def home(request):
    return render(request, 'home.html')


def registrarUsuario(request, tipo):
	a=tipo
	if request.method=='POST':	
		form = UsuarioForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			Group.objects.get_or_create(name="Gerente")
			Group.objects.get_or_create(name="Staff")
			if request.user in Group.objects.get(name="Gerente").user_set.all() or request.user.is_superuser:
				instance.save()
				if a=='Gerente':
					user=User.objects.get(username=instance)
					user.is_staff=True
					user.groups.add(Group.objects.get(name="Gerente"))
					user.save()
					men='El Usuario Gerente ha sido creado exitosamente.'
				else:
					user=User.objects.get(username=instance)
					user.is_staff=True
					user.groups.add(Group.objects.get(name="Staff"))
					user.save()
					men='El Usuario Staff ha sido creado exitosamente.'
				tipo='pos'
				tit='USUARIO CREADO'
			else:
				tipo='neg'
				tit='ACCESO DENEGADO'
				men='No tiene los permisos necesarios para realizar esta tarea.'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
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
			tipo='pos'
			tit='PASSWORD ACTUALIZADO'
			men='El Password ha sido modificado exitosamente.'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})			
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'usuarios/password.html', {'form': form})