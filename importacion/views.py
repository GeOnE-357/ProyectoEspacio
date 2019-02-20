from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
import csv,io
from personas.models import Alumno,Estudio
from cursos.models import Inscripcion,Curso
from .forms import ImportarForm

def importar(request):
	if request.method=="POST":
		form=ImportarForm(request.POST, request.FILES)
		if form.is_valid():
			csv_file=request.FILES['archivo']
			if not csv_file.name.endswith('.csv'):
				tipo='neg'
				tit='ARCHIVO NO VALIDO'
				men='El archivo no tiene formato .csv .'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
			else:
				datos=csv_file.read().decode('latin-1')
				io_string=io.StringIO(datos)
				crea=0
				insc=0
				for fila in csv.reader(io_string, delimiter=';', quotechar="|"):
					
					if Alumno.objects.filter(dni=fila[2]):
						a=Alumno.objects.filter(dni=fila[2])
						print(a)
						if not Inscripcion.objects.filter(alumnoID=a[0]):
							inscribir=Inscripcion()
							inscribir.cursoID=get_object_or_404(Curso,id=fila[10])
							inscribir.alumnoID=get_object_or_404(Alumno,dni=fila[2])
							inscribir.save()
							insc+=1
					else:
						alu=Alumno()
						alu.nombre=fila[0]
						alu.apellido=fila[1]
						alu.dni=fila[2]
						alu.mail=fila[3]
						alu.telefono=fila[4]
						alu.nacimiento=fila[5]
						alu.titulo=fila[6]
						alu.trabajo=fila[7]
						alu.dispHoraria=fila[8]
						alu.estudiosId=get_object_or_404(Estudio,id=fila[9])
						alu.save()
						inscribir=Inscripcion()
						inscribir.cursoID=get_object_or_404(Curso,id=fila[10])
						inscribir.alumnoID=get_object_or_404(Alumno,dni=fila[2])
						inscribir.save()
						insc+=1
						crea+=1
				tipo='pos'
				tit='ALUMNOS REGISTRADOS'
				men='Se han creado '+str(crea)+' Alumnos y se han Inscripto '+str(insc)+' en los cursos.'
				return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
	else:
		form=ImportarForm()
		return render(request, "importacion/importar.html", {'form':form})