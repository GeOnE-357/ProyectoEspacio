from django.shortcuts import render, redirect
from .models import Asistencia
from .forms import AsistenciaForm

def index(request):
    return render(request, 'asistencia/index.html', {
        'cursos': cursos.objects.filter(profesorId=id),
    })
#deberia recibir el id del profesor que 
#loguee y traer las inscripciones de sus cursos
def listar_asist(request):
	pass