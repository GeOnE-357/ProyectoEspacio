from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from dependencia.models import *
# Create your views here.


def dependencias(request):
    return render(request, 'dependencia/dependencias.html', {
        'dependencia': Dependencia.objects.all(),
    })

def aulas(request, id):
	return render (request, 'dependencia/aulas.html',{
		'aulas':Aula.objects.filter(dependenciaId=id)})

def detalleAula(request,id):
	return render(request,'dependencia/detalleAula.html',{
		'detalleA':DetalleAula.objects.filter(aulaId=id)})
   