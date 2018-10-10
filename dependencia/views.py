from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from dependencia.models import *
from .forms import *
# Create your views here.


def dependencias(request):
    return render(request, 'dependencia/dependencias.html', {
        'dependencia': Dependencia.objects.all(),
    })

def aulas(request, id):
	return render (request, 'dependencia/aulas.html',{
		'aulas':Aula.objects.filter(dependenciaId=id),
		})

def detalleAula(request,id):
	return render(request,'dependencia/detalleAula.html',{
		'detalleA':DetalleAula.objects.filter(aulaId=id),
		})

def crearAula(request):
	if request.method=="POST":
		form=AulaForm(request.POST or none)
		if form.is_valid():
			instacia= form.save(commit=False)
			instacia.save()
			return redirect('dependencia')
	else:
		form=AulaForm()
		return render(request, 'dependencia/crearAula.html',{'form':form})

def detalleCrear(request):
       return render(request, 'dependencia/detalleCrear.html')

def dependenciaCrear(request):
	if request.models=="POST":
		form=DependenciaForm(request.POST or none)
		if form.is_valid:
			instacia=form.save(commit=False)
			instacia.save()
			return redirect('dependencia')