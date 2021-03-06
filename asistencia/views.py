from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from datetime import datetime, date, time, timedelta
from django.contrib.auth.models import Group
from .models import Asistencia
from personas.models import Profesor, Alumno
from cursos.models import Curso, Inscripcion
from .forms import AsistenciaForm

def index(request,usuario):
	persona = get_object_or_404(Profesor, dni=usuario)
	curso=Curso.objects.filter(profesorID=persona.id)
	return render(request, 'asistencia/index.html',{'cursos':curso})

def listarAlumnoCurso(request, curso):
	inscripcion=Inscripcion.objects.filter(cursoID=curso)
	curs=get_object_or_404(Curso, id=curso)
	lista=[]
	for ins in inscripcion:
		alumno=[]
		alum=ins.alumnoID
		asis=Asistencia.objects.filter(inscripcionID=ins.id)
		pres=0
		aus=0
		for a in asis:
			if a.presente == True:
				pres += 1
			elif a.presente == False:
				aus +=1
		cur=ins.cursoID	
		clas=cur.cantClases
		alumno.append(alum.id)
		alumno.append(alum.nombre)
		alumno.append(alum.apellido)
		alumno.append(alum.dni)
		alumno.append(alum.mail)
		alumno.append(alum.telefono)
		alumno.append(pres)
		alumno.append(aus)
		alumno.append(clas)
		if aus >= clas/2:
			color="rgba(237,48,48,1)"
			alumno.append(color)
		lista.append(alumno)
	lista.sort(key=lambda presente: presente[6], reverse=True)
	return render (request, 'asistencia/detalle.html', {'lista':lista , 'curso':curs})


def listarAsistenciaCurso(request, curso):
	hoy=date.today()
	inscri=Inscripcion.objects.filter(cursoID=curso).last()
	fecha=Asistencia.objects.filter(inscripcionID=inscri)
	cur=Curso.objects.filter(id=curso)
	if fecha.count() == cur[0].cantClases:
		tipo='pos'
		tit='CURSO FINALIZADO'
		men='El Curso ya ha finalizado, no puedes seguir tomando asistencia.'
		url= '/Asistencia/Mostrar/MisCursos/'+str(cur[0].profesorID.dni)+'/'
		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		if fecha.last() == None or fecha.last().fecha.date() != hoy:
			inscripcion=Inscripcion.objects.filter(cursoID=curso)
			lista=[]
			for ins in inscripcion:
				present=[]
				asist=ins.id
				alumno=ins.alumnoID
				pres=False
				present.append(asist)
				present.append(alumno)
				present.append(pres)
				x=Asistencia.objects.filter(inscripcionID=asist,presente=False)
				if len(x) >= cur[0].cantClases/2:
					color="rgba(237,48,48,1)"
					present.append(color)
				lista.append(present)
			lista.sort(key=lambda presente:presente[2], reverse=True)
			return render (request, 'asistencia/asistencia.html', {'lista':lista})
		else:
			tipo='neg'
			tit='ASISTENCIA YA REALIZADA'
			men='Ya se ha registrado la asistencia de este curso hoy.'
			url= '/Asistencia/Mostrar/MisCursos/'+str(cur[0].profesorID.dni)+'/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	

def AsistenciaCrear(request):
	if request.method=="POST":
		diccionario=request.POST.copy()
		del diccionario['csrfmiddlewaretoken']
		diccionario=diccionario.items()
		lista=list(diccionario)
		asis=[]
		for li in lista:
			if li[1] != 'True' and li[1] != 'False':
				temp=[]
				temp.append(int(li[1]))
			elif li[1] == 'True':
				temp.append(True)
				asis.append(temp)
			else:
				temp.append(False)
				asis.append(temp)	
		for a in asis:
			asistencia=Asistencia()
			asistencia.presente=a[1]
			insc=get_object_or_404(Inscripcion,id=a[0])
			asistencia.inscripcionID=insc
			asistencia.save()
		tipo='pos'
		tit='ASISTENCIA FINALIZADA'
		men='Se ha registrado la asistencia de hoy con éxito.'
		url='/'
		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})

def detalleAsistencia(request, curso, id):
	if request.user.is_authenticated:
		insc=Inscripcion.objects.get(cursoID=curso, alumnoID=id)
		pres=Asistencia.objects.filter(inscripcionID=insc.id)
		return render(request, 'asistencia/presente.html', {'pres':pres, 'insc':insc})
	else:
		tipo='neg'
		tit='ACCESO DENEGADO'
		men='No tiene los permisos necesarios para realizar esta tarea.'
		url='/'
		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})