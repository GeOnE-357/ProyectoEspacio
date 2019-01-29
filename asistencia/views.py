from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Asistencia
from personas.models import Profesor, Alumno
from cursos.models import Curso, Inscripcion
from .forms import AsistenciaForm

def index(request,usuario):
	"""dni=int(usuario) esto convertia el dni STRING en INT, No era necesario."""
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
		asist=0
		for a in asis:
			if a.presente == True:
				asist += 1
		cur=ins.cursoID	
		clas=cur.cantClases
		alumno.append(alum.id)
		alumno.append(alum.nombre)
		alumno.append(alum.apellido)
		alumno.append(alum.dni)
		alumno.append(alum.mail)
		alumno.append(alum.telefono)
		alumno.append(asist)
		alumno.append(clas)
		lista.append(alumno)
	return render (request, 'asistencia/detalle.html', {'lista':lista , 'curso':curs})


def listarAsistenciaCurso(request, curso):

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
		lista.append(present)
	return render (request, 'asistencia/asistencia.html', {'lista':lista})


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
		tit='ASISTENCIA CREADA'
		men='Se ha registrado la asistencia del curso con éxito.'
		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})