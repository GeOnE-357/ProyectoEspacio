from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Curso, Materia, Inscripcion
from personas.models import Profesor, Alumno
from cursos.models import Curso, Materia
from dependencia.models import DetalleAula, Dia, Horario
from .forms import CursoForm, MateriaForm, InscripcionForm
from .filters import CursoFilter, MateriaFilter

def cursosListar(request):
	cursos= Curso.objects.all()
	materias=Materia.objects.all()
	profes=Profesor.objects.all()
	filtro = CursoFilter(request.GET, queryset=cursos)
	lista=[]
	for fi in filtro.qs:
		curso=[]
		curso.append(fi.id)
		curso.append(fi.materiaID)
		curso.append(fi.modulo)
		curso.append(fi.profesorID)
		dias=[]
		det=DetalleAula.objects.filter(estado='en curso', cursoID=fi.id)
		for d in det:
			dia=str(d.aulaId)+": "+str(d.diaId)+" "+str(d.horaId)+":00"
			dias.append(dia)
		curso.append(dias)
		curso.append(fi.estado)
		lista.append(curso)	
	return render(request, 'cursos/index.html', {'filtro':lista, 'materias':materias, 'profes':profes,} )


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


def cursosEditar(request, id):
	if request.method=="POST":
		curso=get_object_or_404(Curso, id=id)
		form = CursoForm(request.POST, instance=curso)
		if form.is_valid:
			form.save(commit=False)
			form.save()
			return redirect('cursos-index')
	else:
		curso=get_object_or_404(Curso, id=id)
		form = CursoForm(instance=curso)
	return render(request, 'cursos/editar.html', {'form':form})


def materiasListar(request):
	materias=Materia.objects.all()
	filtro = MateriaFilter(request.GET, queryset=materias)
	return render(request, 'materias/index.html', {'filtro':filtro})


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

def materiasEditar(request, id):
	if request.method=="POST":
		materia=get_object_or_404(Materia, id=id)
		form=MateriaForm(request.POST, instance=materia)
		if form.is_valid:
			form.save(commit=False)
			form.save()
			return redirect('materias-index')
	else:
		materia=get_object_or_404(Materia, id=id)
		form=MateriaForm(instance=materia)
	return render(request, 'materias/editar.html', {'form':form})

def inscripcionCrear(request, tipo, id):
	a=tipo
	if request.method=="POST":
		form=InscripcionForm(request.POST or none)
		if form.is_valid():
			instance=form.save(commit=False)
			alumno=get_object_or_404(Alumno, id=id)
			instance.alumnoID=alumno
			form.save()
			return redirect('personas-index', a)
	else:
		form=InscripcionForm()
	return render(request, 'cursos/inscripcion.html', {'form':form})