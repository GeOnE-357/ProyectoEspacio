from django.shortcuts import render, redirect, get_object_or_404
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
		'nueve':DetalleAula.objects.filter(aulaId=id, horaId=1),
		'diez':DetalleAula.objects.filter(aulaId=id, horaId=2),
		'once':DetalleAula.objects.filter(aulaId=id, horaId=3),
		'doce':DetalleAula.objects.filter(aulaId=id, horaId=4),
		'trece':DetalleAula.objects.filter(aulaId=id, horaId=5),
		'catorce':DetalleAula.objects.filter(aulaId=id, horaId=6),
		'quince':DetalleAula.objects.filter(aulaId=id, horaId=7),
		'dieciseis':DetalleAula.objects.filter(aulaId=id, horaId=8),
		'diecisiete':DetalleAula.objects.filter(aulaId=id, horaId=9),
		'dieciocho':DetalleAula.objects.filter(aulaId=id, horaId=10),
		'diecinueve':DetalleAula.objects.filter(aulaId=id, horaId=11),
		'veinte':DetalleAula.objects.filter(aulaId=id, horaId=12),
		'veintiuno':DetalleAula.objects.filter(aulaId=id, horaId=13),
		'veintidos':DetalleAula.objects.filter(aulaId=id, horaId=14),
		'veintitres':DetalleAula.objects.filter(aulaId=id, horaId=15),
		'aula':Aula.objects.filter(id=id),
		'dia':Dia.objects.all(),
		'hora':Horario.objects.all(),
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
