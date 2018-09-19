from django.shortcuts import render
from dependencia.models import *
# Create your views here.

def dependencias(request):
    return render(request, 'dependencia/dependencias.html', {
        'dependencia': Dependencia.objects.all(),
        
    })