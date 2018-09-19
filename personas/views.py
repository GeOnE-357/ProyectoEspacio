from django.shortcuts import render, redirect, get_object_or_404
from personas.models import *
from .forms import profesorForm, alumnoForm

def personasListar(request):
    return render(request, 'personas/index.html', {
        'profesores': Profesor.objects.all(),
        'alumnos': Alumno.objects.all()
    })

def profesorNuevo(request):
	if request.method == "POST":
		form = profesorForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('personas-index')
	else:
		form = profesorForm()
	return render(request, 'personas/crear.html', {'form':form})


def alumnoNuevo(request):
	if request.method == "POST":
		form = alumnoForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
	else:
		form = alumnoForm()
	return render(request, 'personas/crear.html', {'form':form})
