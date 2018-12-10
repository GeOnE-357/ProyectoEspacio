from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Asistencia
from personas.models import Profesor, Alumno
from cursos.models import Curso, Inscripcion
from .forms import AsistenciaForm

def index(request,usuario):
	"""dni=int(usuario) esto convertia el dni STRING en INT, No era necesario."""
	persona = get_object_or_404(Profesor, dni=usuario)
	curso=Curso.objects.filter(profesorID=persona.id)
	return render(request, 'asistencia/index.html',{'cursos':curso})

def listarAlumnoCurso(request, curso):
	inscriptos=get_list_or_404(Inscripcion, cursoID=curso)
	lista=[]
	for a in inscriptos:
		alumno=get_object_or_404(Alumno, id=a.alumnoID)
		lista.append(alumno)
	return render (request, 'asistencia/detalle.html', {'lista':lista})