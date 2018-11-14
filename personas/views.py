from django.shortcuts import render, redirect, get_object_or_404
from personas.models import *
from espacio.forms import UsuarioForm
from .forms import profesorForm, alumnoForm
from .filters import ProfesorFilter, AlumnoFilter

def personasListar(request, tipo):
	a=tipo
	if a == 'Profesor':
		personas = Profesor.objects.all()
		filtro = ProfesorFilter(request.GET, queryset=personas)
		return render(request, 'personas/index.html', {
			'personas':personas, 'filtro':filtro, 'tipo':a})
	else:
		personas = Alumno.objects.all()
		filtro = AlumnoFilter(request.GET, queryset=personas)
		return render(request, 'personas/index.html', {
			'personas':personas, 'filtro':filtro, 'tipo':a})


def personaNuevo(request, tipo):
	a=tipo
	if request.method == "POST":
		if a =="Profesor":
			form = profesorForm(request.POST or None)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				return redirect('personas-index', a)
		else:
			form = alumnoForm(request.POST or None)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				return redirect('personas-index', a)
	else:
		if a =="Profesor":
			form = profesorForm()
		else:
			form = alumnoForm()
	return render(request, 'personas/crear.html', {'form':form})


def personaDetalle(request, tipo, id):
	a=tipo
	if a == 'Profesor':
		persona = Profesor.objects.get(id=id)
		return render(request, 'personas/detalle.html', {'Profesor':persona, 'tipo':a})
	else:
		persona = Alumno.objects.get(id=id)
		return render(request, 'personas/detalle.html', {'Alumno':persona, 'tipo':a})


def personaEditar(request, tipo, id):
	a=tipo
	if a == 'Profesor':
		persona = get_object_or_404(Profesor, id=id)
		form = profesorForm(request.POST, instance=persona)
		if form.is_valid():
				form.save(commit=False)
				form.save()
				return redirect('personas-index', a)
		else:
			form = profesorForm(instance=persona)		
		return render(request, 'personas/modificar.html', {'form':form})