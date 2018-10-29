from django.shortcuts import render, redirect
from .models import Curso, Materia, Mes, Asistencia
from .forms import CursoForm, MateriaForm

def cursosListar(request):
	return render(request, 'cursos/index.html', {'cursos': Curso.objects.all()})


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