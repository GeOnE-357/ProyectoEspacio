from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Curso, Materia, Inscripcion
from personas.models import Profesor
from .forms import CursoForm, MateriaForm, InscripcionForm
from .filters import CursoFilter

def cursosListar(request):
	cursos= Curso.objects.all()
	materias = Materia.objects.all()
	profes = Profesor.objects.all()
	filtro = CursoFilter(request.GET, queryset=cursos)
	return render(request, 'cursos/index.html', {'filtro':filtro, 'materias':materias, 'profes':profes} )


def cursosCrear(request):
	if request.method=="POST":
		form=CursoForm(request.POST or none)
		if form.is_valid():
			instacia= form.save(commit=False)
			instacia.save()
			return redirect('cursos-index')
	else:
		form=CursoForm()
	return render(request, 'cursos/crear.html', {'form':form})


def materiasListar(request):
	return render(request, 'materias/index.html', {'materias': Materia.objects.all()})


def materiasCrear(request):
	if request.method=="POST":
		form=MateriaForm(request.POST or none)
		if form.is_valid():
			instacia= form.save(commit=False)
			instacia.save()
			return redirect('materias-index')
	else:
		form=MateriaForm()
	return render(request, 'materias/crear.html', {'form':form})


def inscripcionCrear(request, id):
	if request.method=="POST":
		form=InscripcionForm(request.POST or none)
		if form.is_valid():
			instancia= form.save(commit=False)
			instancia.save()
	else:
		form=InscripcionForm()
	return render(request, 'cursos/inscripcion.html', {'form':form})