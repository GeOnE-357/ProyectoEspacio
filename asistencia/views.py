from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Asistencia
from personas.models import Profesor
from cursos.models import Curso
from .forms import AsistenciaForm

def index(request,usuario):
	"""dni=int(usuario)"""
	persona = get_object_or_404(Profesor, dni=usuario)
	curso=Curso.objects.filter(profesorID=persona.id)
	return render(request, 'asistencia/index.html',{'cursos':curso})

def listarCurso(request):
	return render(request, 'asistencia/detalleCurso',{
		'inscriptos': Inscripcion.objects.filter(estado='vigente')})
