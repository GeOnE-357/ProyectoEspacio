from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import Group
from django.http import HttpResponse
from dependencia.models import *
from .forms import *
from cursos.models import Curso
from .filters import DependenciaFilter, AulaFilter

MES_CHOICES = (
	("enero", "Enero"),
	("febrero", "Febrero"),
	("marzo", "Marzo"),
	("abril", "Abril"),
	("mayo", "Mayo"),
	("junio", "Junio"),
	("julio", "Julio"),
	("agosto", "Agosto"),
	("septiembre", "Septiembre"),
	("octubre", "Octubre"),
	("noviembre", "Noviembre"),
	("diciembre", "Diciembre"),)

def dependencias(request):
	depen= Dependencia.objects.all()
	filtro = DependenciaFilter(request.GET, queryset=depen)
	return render(request, 'dependencia/dependencias.html', {'filtro':filtro,})

def aulasLista(request, id):
	aula= Aula.objects.filter(dependenciaId=id)
	filtro = AulaFilter(request.GET, queryset=aula)
	depen= Dependencia.objects.filter(id=id)
	lista=[]
	for b in aula:
		det=DetalleAula.objects.filter(aulaId=b.id)
		anios=[]
		for c in det:
			anios.append(c.anio)
		anios=list(set(anios))
		if anios:
			temp=[]
			temp.append(b.id)
			for c in anios:
				temp.append(c)
			lista.append(temp)
	listaB=[]
	for c in MES_CHOICES:
		for a in lista:
			for b in a:
				pri=DetalleAula.objects.all().filter(aulaId=a[0], mes=c[0], anio=b).first()
				if pri:
					mesA=[]
					mesA.append(a[0])
					mesA.append(pri.mes)
					mesA.append(pri.anio)
					listaB.append(mesA)
	return render (request, 'dependencia/aulas.html',{'filtro':filtro, 'depen':depen, 'lista':listaB})

def aula(request,id):
	if request.method=="POST":
		form=MesForm(request.POST or none)
		if form.is_valid:
			diccionario=request.POST.copy()
			del diccionario['csrfmiddlewaretoken']
			mes=diccionario['mes']
			anio=diccionario['anio']    
			return redirect('horarioCrear',id,mes,anio)
	else:
		aula=get_object_or_404(Aula, id=id)
		form=MesForm()
		return render(request,'dependencia/aula.html',{'aula':aula,'form':form})

def aulaMes(request,id,mes,anio):
	detalle=DetalleAula.objects.filter(aulaId=id,mes=mes,anio=anio).order_by('horaId', 'diaId')
	aula=get_object_or_404(Aula, id=id)
	dia=get_list_or_404(Dia)
	anio=anio
	mes=mes
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
			modif=det.id
			detalle.append(curso)
			detalle.append(modif)
			lista.append(detalle)
	return render(request,'dependencia/aulaMes.html',{'aula':aula, 'lista':lista, 'dia':dia, 'anio':anio, 'mes':mes})

def crearAula(request, id):
	if request.method=="POST":
		group = Group.objects.get(name="Gerente").user_set.all()
		if request.user in group or request.user.is_superuser:
			form=AulaForm(request.POST or none)
			if form.is_valid():
				depen=get_object_or_404(Dependencia, id=id)
				instancia= form.save(commit=False)
				instancia.dependenciaId=depen
				instancia.save()
				tipo='pos'
				tit='AULA CREADA'
				men='El Aula ha sido creada exitosamente.'
				url='/Dependencia/Mostrar/Aulas/'+str(depen.id)
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			url='/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		form=AulaForm()
		return render(request, 'dependencia/crearAula.html',{'form':form})

def horarioCrear(request, aula, mes, anio):
	group = Group.objects.get(name="Gerente").user_set.all()
	if request.user in group or request.user.is_superuser:  
		a=get_object_or_404(Aula, id=aula)
		b=DetalleAula.objects.filter(aulaId=aula, mes=mes, anio=anio)
		if b:
			tipo='neg'
			tit='HORARIO EXISTENTE'
			men='Los horarios del Aula que intenta crear ya existen.'
			url='/Dependencia/Mostrar/Aula/'+aula+'/'+mes+'/'+anio+'/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})	
		else:
			for d in Dia.objects.all():
				for h in Horario.objects.all():
					det=DetalleAula()
					det.aulaId=a
					det.diaId=d
					det.estado="disponible"
					det.horaId=h
					det.mes=mes
					det.anio=anio
					det.save()
			tipo='pos'
			tit='HORARIO CREADO'
			men='Los horarios del Aula han sido creada exitosamente.'
			url='/Dependencia/Mostrar/Aula/'+aula+'/'+mes+'/'+anio+'/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		tipo='neg'
		tit='ACCESO DENEGADO'
		men='No tiene los permisos necesarios para realizar esta tarea.'
		url='/'
		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})

def horarioCopiar(request, id):
	if request.method=="POST":
		group = Group.objects.get(name="Gerente").user_set.all()
		if request.user in group or request.user.is_superuser:
			diccionario=request.POST.copy()
			del diccionario['csrfmiddlewaretoken']
			diccionario=dict(diccionario)
			if diccionario['mes'][0]==diccionario['mesCopia'][0] and diccionario['anio'][0]==diccionario['anioCopia'][0]:
				tipo='neg'
				tit='MISMO MES'
				men='Los meses seleccionados son exactamente los mismos.'
				url='/Dependencia/Copiar/Aula/Horarios/'+str(id)
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
			else:
				mes=DetalleAula.objects.filter(aulaId=id, mes=diccionario['mes'][0], anio=diccionario['anio'][0])
				mes=list(mes.order_by('horaId', 'diaId'))
				copia=DetalleAula.objects.filter(aulaId=id, mes=diccionario['mesCopia'][0], anio=diccionario['anioCopia'][0])
				copia=list(copia.order_by('horaId', 'diaId'))
				for n, a in enumerate(mes):
					copia[n].estado=a.estado
					copia[n].cursoID=a.cursoID
					copia[n].save()		
				tipo='pos'
				tit='MES COPIADO'
				men='Los cursos del mes han sido copiados exitosamente.'
				url='/Dependencia/Mostrar/Aula/'+str(id)+'/'+str(diccionario['mesCopia'][0])+'/'+str(diccionario['anioCopia'][0])+'/'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		aula= Aula.objects.filter(id=id)
		lista=[]
		meses=[]
		anios=[]
		for b in aula:
			for a in MES_CHOICES:
				mes=DetalleAula.objects.filter(aulaId=b.id, mes=a[0]).values()
				mes=list(mes)
				if mes:
					mes=mes[0]
					meses.append(mes['mes'])
					anios.append(mes['anio'])
			meses=list(set(meses))
			anios=list(set(anios))
			aulaid=b.id
		return render(request, 'dependencia/copiarMes.html', {'meses':meses, 'anios':anios, 'aula':aulaid})


def detalleEditar(request, id):
	if request.method=="POST":
		group = Group.objects.get(name="Gerente").user_set.all()
		if request.user in group or request.user.is_superuser:
			detalle=get_object_or_404(DetalleAula, id=id)
			form = DetalleAulaForm(request.POST, instance=detalle)
			if form.is_valid():
				form.save(commit=False)
				form.save()
				tipo='pos'
				tit='AULA EDITADA'
				men='El Aula ha sido editada exitosamente.'
				url='/Dependencia/Mostrar/Aula/'+str(detalle.aulaId.id)+'/'+str(detalle.mes)+'/'+str(detalle.anio)+'/'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			url='/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		detalle=get_object_or_404(DetalleAula, id=id)
		form = DetalleAulaForm(instance=detalle)
	return render(request, 'dependencia/detalleEditar.html', {'form':form})


def dependenciaCrear(request):
	if request.method=="POST":
		group = Group.objects.get(name="Gerente").user_set.all()
		if request.user in group or request.user.is_superuser:
			form=DependenciaForm(request.POST or none)
			if form.is_valid:
				instacia=form.save(commit=False)
				instacia.save()
				tipo='pos'
				tit='DEPENDENCIA CREADA'
				men='La Dependencia ha sido creada exitosamente.'
				url='/Dependencia/'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			url='/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		form=DependenciaForm()
		return render(request,'dependencia/dependenciacrear.html',{'form':form})

def cargarCurso(request, id, mes, anio, tipo):
	if request.method=="POST":
		group = Group.objects.get(name="Gerente").user_set.all()
		if request.user in group or request.user.is_superuser:
			form=CargarCursoForm(request.POST or none)
			if form.is_valid:
				diccionario=request.POST.copy()
				del diccionario['csrfmiddlewaretoken']
				diccionario=dict(diccionario)
				dias=[]
				horas=[]
				for a, b in diccionario.items():
					if a=="dia":
						for x in b:
							dias.append(x)
					if a=='hora1' or a=='hora2':
						horas.append(int(b[0]))
				for d in dias:
					detalle=DetalleAula.objects.filter(aulaId=id,mes=mes,anio=anio,diaId=d).order_by('horaId')
					for det in detalle:
						if det.horaId.id>=horas[0] and det.horaId.id<=horas[1]:
							det.cursoID=Curso.objects.get(id=diccionario['curso'][0])
							det.estado="en curso"
							det.save()
				tipo='pos'
				tit='CURSOS ASIGNADOS'
				men='El Curso ha sido creada exitosamente.'
				url='/Dependencia/Mostrar/Aula/'+str(id)+'/'+mes+'/'+anio+'/'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			url='/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		if tipo == 'cargar':
			form=CargarCursoForm()
			return render(request,'dependencia/curso.html',{'form':form})
		else:
			detalle=DetalleAula.objects.filter(aulaId=id,mes=mes,anio=anio).order_by('horaId', 'diaId')
			for det in detalle:
				det.estado="disponible"
				det.cursoID=None
				det.save()
			tipo='pos'
			tit='CURSO VACIO'
			men='El Curso ha sido vaciado exitosamente.'
			url='/Dependencia/Mostrar/Aula/'+str(id)+'/'+mes+'/'+anio+'/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})