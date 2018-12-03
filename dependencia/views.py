from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from dependencia.models import *
from .forms import *
from cursos.models import Curso
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
		'detalleA':DetalleAula.objects.filter(aulaId=id).order_by('horaId'),
		'aula':get_list_or_404(Aula, id=id),
		'dia':get_list_or_404(Dia),
		'hora':get_list_or_404(Horario),
		})

def crearAula(request):
	if request.method=="POST":
		form=AulaForm(request.POST or none)
		if form.is_valid():
			instacia= form.save(commit=False)
			instacia.save()
			return redirect('detallecrear')
	else:
		form=AulaForm()
		return render(request, 'dependencia/crearAula.html',{'form':form})

def detalleCrear(request):	
	a=Aula.objects.latest('id')
	for d in Dia.objects.all():
		for h in Horario.objects.all():
			det=DetalleAula()
			det.aulaId=a
			det.diaId=d
			det.estado="disponible"
			det.horaId=h
			det.save()
	return redirect('dependencia')

def dependenciaCrear(request):
	if request.method=="POST":
		form=DependenciaForm(request.POST or none)
		if form.is_valid:
			instacia=form.save(commit=False)
			instacia.save()
			return redirect('dependencia')
	else:
		form=DependenciaForm()
		return render(request,'dependencia/dependenciacrear.html',{'form':form})
