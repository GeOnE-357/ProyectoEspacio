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

def detalleCrear():
	aula=DetalleAula.objects.latest(id)
	form=DetalleAulaForm()
	d=0
	i=0
	while i<8:
		dia=i+1
		while d<15:
			hora=d+1
			instacia=form.save(commit=False)
			instacia.aulaid=Aula.objects.get(aula)
			instacia.diaId=Dia.objects.get(id=dia)
			instacia.estado="disponible"
			instacia.horaId=Horario.objects.get(id=hora)
			instacia.save()
			d=d+1
		d=0
		i=i+1
	return render('dependencia')

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
