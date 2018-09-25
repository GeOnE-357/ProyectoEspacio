from django.shortcuts import render, redirect, get_object_or_404
from personas.models import *
from .forms import profesorForm, alumnoForm

def personasListar(request, tipo):
	a=tipo
	if a == 'Profesor':
		return render(request, 'personas/index.html', {
			'personas': Profesor.objects.all(), 'tipo':a})
	else:
		return render(request, 'personas/index.html', {
			'personas': Alumno.objects.all(), 'tipo':a})


def personaNuevo(request, tipo):
	a=tipo
	if request.method == "POST":
		if a =="Profesor":
			form = profesorForm(request.POST or None)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				return redirect('personas-index')
		else:
			form = alumnoForm(request.POST or None)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				return redirect('personas-index')
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