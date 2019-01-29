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
	detalle=DetalleAula.objects.filter(aulaId=id).order_by('horaId', 'diaId')
	aula=get_object_or_404(Aula, id=id)
	dia=get_list_or_404(Dia)
	lista=[]
	for det in detalle:
		if det.estado == "disponible":
			detalle=[]
			modif=det.id
			esta=det.estado
			detalle.append(esta)
			detalle.append(modif)
			lista.append(detalle)
		else:
			detalle=[]
			curso=det.cursoID
			materia=curso.materiaID
			modulo=curso.modulo
			modif=det.id
			detalle.append(materia)
			detalle.append(modulo)
			detalle.append(modif)
			lista.append(detalle)
	return render(request,'dependencia/detalleAula.html',{'aula':aula, 'lista':lista, 'dia':dia})

def crearAula(request):
	if request.method=="POST":
		form=AulaForm(request.POST or none)
		if form.is_valid():
			instacia= form.save(commit=False)
			instacia.save()
			a=Aula.objects.latest('id').id
			return redirect('detallecrear', a)
	else:
		form=AulaForm()
		return render(request, 'dependencia/crearAula.html',{'form':form})

def detalleCrear(request, aula):	
	a=get_object_or_404(Aula, id=aula)
	for d in Dia.objects.all():
		for h in Horario.objects.all():
			det=DetalleAula()
			det.aulaId=a
			det.diaId=d
			det.estado="disponible"
			det.horaId=h
			det.save()
	tipo='pos'
	tit='AULA CREADA'
	men='El Aula ha sido creada exitosamente.'
	return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})

def detalleEditar(request, id):
	if request.method=="POST":
		detalle=get_object_or_404(DetalleAula, id=id)
		form = DetalleAulaForm(request.POST, instance=detalle)
		if form.is_valid():
			form.save(commit=False)
			form.save()
			tipo='pos'
			tit='AULA EDITADA'
			men='El Aula ha sido editada exitosamente.'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
	else:
		detalle=get_object_or_404(DetalleAula, id=id)
		form = DetalleAulaForm(instance=detalle)
	return render(request, 'dependencia/detalleEditar.html', {'form':form})


def dependenciaCrear(request):
	if request.method=="POST":
		form=DependenciaForm(request.POST or none)
		if form.is_valid:
			instacia=form.save(commit=False)
			instacia.save()
			tipo='pos'
			tit='DEPENDENCIA CREADA'
			men='La Dependencia ha sido creada exitosamente.'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
	else:
		form=DependenciaForm()
		return render(request,'dependencia/dependenciacrear.html',{'form':form})
