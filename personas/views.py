from django.shortcuts import render, redirect
from personas.models import *

def personasListar(request):
    return render(request, 'personas/index.html', {
        'profesores': Profesor.objects.all(),
        'alumnos': Alumno.objects.all()
    })