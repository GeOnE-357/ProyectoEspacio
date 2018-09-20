from django.shortcuts import render
from django.http import HttpResponse
from dependencia.models import *
# Create your views here.

def indexDependencia(request):
    return HttpResponse("pag principal...En construccion")

def dependencias(request):
    return render(request, 'dependencia/dependencias.html', {
        'dependencia': Dependencia.objects.all(),
        
    })
    