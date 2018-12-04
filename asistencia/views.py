from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Asistencia
from .forms import AsistenciaForm

def index(request,usuario):
	profe: profesor.objects.filter(dni=usuario)
	cur:cursos.objects.filter(profesorId=profe.id,estado='vigente')
	return render(request, 'asistencia/index.html')
#deberia recibir el user del profesor que 
#loguee y traer las inscripciones de sus cursos
def listarCurso(request):
	return render(request, 'asistencia/detalleCurso',{
		'inscriptos': Inscripcion.objects.filter(estado='vigente'),
		})
