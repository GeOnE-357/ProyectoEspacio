from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from datetime import datetime
import csv,io
from personas.models import Alumno
from cursos.models import Inscripcion,Curso
from .forms import ImportarForm

def importar(request):
	if request.method=="POST":
		if request.user.is_staff:
			form=ImportarForm(request.POST, request.FILES)
			if form.is_valid():
				csv_file=request.FILES['archivo']
				if not csv_file.name.endswith('.csv'):
					tipo='neg'
					tit='ARCHIVO NO VALIDO'
					men='El archivo no tiene formato .csv .'
					url='/'
					return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
				else:
					datos=csv_file.read().decode('latin-1')
					io_string=io.StringIO(datos)
					crea=0
					insc=0
					count=0;
					for fila in csv.reader(io_string, delimiter=';', quotechar="|"):
						if count!=0:
							if Alumno.objects.filter(dni=int(fila[2])):
								a=Alumno.objects.filter(dni=fila[2])
								if not Inscripcion.objects.filter(alumnoID=a[0]):
									inscribir=Inscripcion()
									inscribir.cursoID=get_object_or_404(Curso,id=fila[8])
									inscribir.alumnoID=get_object_or_404(Alumno,dni=fila[2])
									inscribir.save()
									insc+=1
							else:
								alu=Alumno()
								alu.nombre=fila[0].title()
								alu.apellido=fila[1].title()
								alu.dni=fila[2]
								alu.mail=fila[3]
								alu.telefono=fila[4]
								fecha=datetime.strptime(fila[5],'%d/%m/%Y')
								alu.nacimiento=fecha.strftime('%Y-%m-%d')
								alu.trabajo=fila[6]
								alu.estudios=fila[7]
								alu.save()
								inscribir=Inscripcion()
								inscribir.cursoID=get_object_or_404(Curso,id=fila[8])
								inscribir.alumnoID=get_object_or_404(Alumno,dni=fila[2])
								inscribir.save()
								insc+=1
								crea+=1
						else:
							count+=1
							continue
					tipo='pos'
					tit='ALUMNOS REGISTRADOS'
					men='Se han creado '+str(crea)+' Alumnos y se han Inscripto '+str(insc)+' en los cursos.'
					url='/Importacion/'
					return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
		else:
			tipo='neg'
			tit='ACCESO DENEGADO'
			men='No tiene los permisos necesarios para realizar esta tarea.'
			url='/'
			return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men, 'url':url})
	else:
		form=ImportarForm()
		return render(request, "importacion/importar.html", {'form':form})