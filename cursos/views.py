from django.shortcuts import render
from .models import Curso, Materia, Mes, Asistencia

def cursosListar(request):
	return render(request, 'cursos/index.html', {'cursos': Curso.objects.all()})


def materiasListar(request):
	return render(request, 'materias/index.html', {'materias': Materia.objects.all()})
