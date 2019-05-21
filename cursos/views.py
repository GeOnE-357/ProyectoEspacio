from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import Group
from .models import Curso, Materia, Inscripcion
from personas.models import Profesor, Alumno
from cursos.models import Curso, Materia
from dependencia.models import DetalleAula, Dia, Horario
from .forms import CursoForm, MateriaForm, InscripcionForm
from .filters import CursoFilter, MateriaFilter

def cursosListar(request):
	cursos= Curso.objects.all()
	filtro = CursoFilter(request.GET, queryset=cursos)
	lista=[]
	for fi in filtro.qs:
		curso=[]
		curso.append(fi.id)
		curso.append(fi.materiaID)
		curso.append(fi.modulo)
		curso.append(fi.profesorID)
		dias=[]
		hor=[]
		semana=Dia.objects.all()
		for a in semana:
			det=DetalleAula.objects.filter(estado='en curso', cursoID=fi.id, diaId=a.id)
			if det:
				dias.append(det)
		for d in dias:
			dia=str(d[0].diaId)+" de "+str(d[0].horaId)+":00 a "+str(d.last().horaId)+":00 en "+str(d[0].aulaId)+"."
			hor.append(dia)
		curso.append(hor)
		curso.append(fi.estado)
		lista.append(curso)	
	return render(request, 'cursos/index.html', {'filtro':lista, 'formu':filtro,} )


def cursosCrear(request):
	if request.method=="POST":
		group = Group.objects.get(name="Gerente").user_set.all()
		if request.user in group or request.user.is_superuser:
			form=CursoForm(request.POST or none)
			if form.is_valid():
				instacia= form.save(commit=False)
				instacia.save()
				tipo='pos'
				tit='CURSO CREADO'
				men='El Curso ha sido creado exitosamente.'
				url='/Curso/'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			url='/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		form=CursoForm()
	return render(request, 'cursos/crear.html', {'form':form})


def cursosEditar(request, id):
	if request.method=="POST":
		group = Group.objects.get(name="Gerente").user_set.all()
		if request.user in group or request.user.is_superuser:
			curso=get_object_or_404(Curso, id=id)
			form = CursoForm(request.POST, instance=curso)
			if form.is_valid:
				form.save(commit=False)
				form.save()
				tipo='pos'
				tit='CURSO EDITADO'
				men='El Curso ha sido editado exitosamente.'
				url='/Curso/'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			url='/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		curso=get_object_or_404(Curso, id=id)
		form = CursoForm(instance=curso)
	return render(request, 'cursos/editar.html', {'form':form})


def materiasListar(request):
	materias= Materia.objects.all()
	filtro = MateriaFilter(request.GET, queryset=materias)
	return render(request, 'materias/index.html', {'filtro':filtro})


def materiasCrear(request):
	if request.method=="POST":
		group = Group.objects.get(name="Gerente").user_set.all()
		if request.user in group or request.user.is_superuser:
			form=MateriaForm(request.POST or none)
			if form.is_valid():
				instacia= form.save(commit=False)
				instacia.save()
				tipo='pos'
				tit='MATERIA CREADA'
				men='La Materia ha sido creada exitosamente.'
				url='/Curso/Materia/'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			url='/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		form=MateriaForm()
	return render(request, 'materias/crear.html', {'form':form})

def materiasEditar(request, id):
	if request.method=="POST":
		group = Group.objects.get(name="Gerente").user_set.all()
		if request.user in group or request.user.is_superuser:
			materia=get_object_or_404(Materia, id=id)
			form=MateriaForm(request.POST, instance=materia)
			if form.is_valid:
				form.save(commit=False)
				form.save()
				tipo='pos'
				tit='MATERIA EDITADA'
				men='La Materia ha sido editada exitosamente.'
				url='/Curso/Materia/'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			url='/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		materia=get_object_or_404(Materia, id=id)
		form=MateriaForm(instance=materia)
	return render(request, 'materias/editar.html', {'form':form})

def inscripcionCrear(request, tipo, id):
	a=tipo
	if request.method=="POST":
		if request.user.is_staff:
			form=InscripcionForm(request.POST or none)	
			insc=Inscripcion.objects.filter(cursoID=form['cursoID'].value(), alumnoID=id)
			if insc:
				tipo='neg'
				tit='INSCRIPCIÓN YA CREADA'
				men='El Alumno ha sido inscripto anteriormente.'
				url='/'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
			else:
				if form.is_valid():
					instance=form.save(commit=False)
					alumno=get_object_or_404(Alumno, id=id)
					instance.alumnoID=alumno
					form.save()
					tipo='pos'
					tit='INSCRIPCIÓN CREADA'
					men='El Alumno ha sido inscripto exitosamente.'
					url='/Persona/Alumno/'
					return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			url='/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		form=InscripcionForm()
	return render(request, 'cursos/inscripcion.html', {'form':form})