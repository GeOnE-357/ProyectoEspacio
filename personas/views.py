from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from personas.models import *
from django.contrib.auth.models import User
from espacio.forms import UsuarioForm
from .forms import profesorForm, alumnoForm
from .filters import ProfesorFilter, AlumnoFilter

def personasListar(request, tipo):
	a=tipo
	if a == 'Profesor':
		personas = Profesor.objects.all()
		filtro = ProfesorFilter(request.GET, queryset=personas)
		return render(request, 'personas/index.html', {'filtro':filtro, 'tipo':a})
	else:
		personas = Alumno.objects.all()
		filtro = AlumnoFilter(request.GET, queryset=personas)
		return render(request, 'personas/index.html', {'filtro':filtro, 'tipo':a})


def personaNuevo(request, tipo):
	a=tipo
	if request.method == "POST":
		if a =="Profesor":
			if request.user.is_superuser:
				form = profesorForm(request.POST or None)
				prof=Profesor.objects.all()
				ban=0
				for p in prof:
					if int(request.POST["dni"]) == int(p.dni):
						ban=1
				if ban == 0:
					if form.is_valid():
						instance = form.save(commit=False)
						estu=Estudio.objects.get(id=form['estudiosId'].value())
						instance.estudiosId=estu
						instance.save()
						return redirect('persona-usuario', a)
				else:
					tipo='neg'
					tit='PROFESOR NO CREADO'
					men='El Profesor ya existe en la base de datos.'
					return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})	
			else:
				tipo='neg'
				tit='ACCESO DENEGADO'
				men='No tiene los permisos necesarios para realizar esta tarea.'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})		
		else:
			form = alumnoForm(request.POST or None)
			alu=Alumno.objects.all()
			ban=0
			for a in alu:
				if int(request.POST["dni"]) == int(a.dni):
					ban=1
			if ban == 0:
				if form.is_valid():
					instance = form.save(commit=False)
					estu=Estudio.objects.get(id=form['estudiosId'].value())
					instance.estudiosId=estu
					instance.save()
					tipo='pos'
					tit='ALUMNO CREADO'
					men='El Alumno ha sido creado exitosamente.'
					return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
			else:
				tipo='neg'
				tit='ALUMNO NO CREADO'
				men='El Alumno ya existe en la base de datos.'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
			
	else:
		if a =="Profesor":
			form = profesorForm()
		else:
			form = alumnoForm()
	return render(request, 'personas/crear.html', {'form':form})


def personaUsuario(request, tipo):
	a=tipo
	if request.user.is_staff:
		profe=Profesor.objects.latest('id')
		nombre=profe.nombre
		apellido=profe.apellido
		mail=profe.mail
		dni=profe.dni
		usuario=User.objects.create_user(username=dni, first_name=nombre, last_name=apellido ,email=mail, password='EDLT1234')
		usuario.save()
		tipo='pos'
		tit='USUARIO CREADO'
		men='El Profesor ha sido creado exitosamente.'
		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})

def personaDetalle(request, tipo, id):
	a=tipo
	if a == 'Profesor':
		persona = get_object_or_404(Profesor, id=id)
		return render(request, 'personas/detalle.html', {'Profesor':persona, 'tipo':a})
	else:
		persona = get_object_or_404(Alumno, id=id)
		return render(request, 'personas/detalle.html', {'Alumno':persona, 'tipo':a})


def personaEditar(request, tipo, id):
	a=tipo
	if request.method=="POST":
			if a == 'Profesor':
				if request.user.is_superuser:
					persona = get_object_or_404(Profesor, id=id)
					form = profesorForm(request.POST, instance=persona)
					if form.is_valid():
							form.save(commit=False)
							form.save()
							tipo='pos'
							tit='PROFESOR EDITADO'
							men='Los datos del Profesor han sido editados exitosamente.'
							return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
				else:
					tipo='neg'
					tit='ACCESO DENEGADO'
					men='No tiene los permisos necesarios para realizar esta tarea.'
					return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
			else:
				persona = get_object_or_404(Alumno, id=id)
				form = alumnoForm(request.POST, instance=persona)
				if form.is_valid():
						form.save(commit=False)
						form.save()
						tipo='pos'
						tit='ALUMNO EDITADO'
						men='Los datos del Alumno han sido editados exitosamente.'
						return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})			
	else:
		if a == 'Profesor':
			persona = get_object_or_404(Profesor, id=id)
			form = profesorForm(instance=persona)
		else:
			persona = get_object_or_404(Alumno, id=id)
			form = alumnoForm(instance=persona)					
	return render(request, 'personas/modificar.html', {'form':form})