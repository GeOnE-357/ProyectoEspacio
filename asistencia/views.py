from django.shortcuts import render, redirect
from .models import Asistencia
from .forms import AsistenciaForm

def index(request):
    return render(request, 'asistencia/index.html', {
        'asist': Asistencia.objects.all(),
    })
