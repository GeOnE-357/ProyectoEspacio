from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib import messages
import csv,io
from personas.models import Alumno,Estudio
from cursos.models import Inscripcion,Curso

def importar(request):
	prompt={
		'datos':"El orden debe ser nombre,apellido,dni,mail,telefono,nacimiento,titulo,trabajo,disponibilidad, estudios, curso"
	}
	if request.method== "GET":
		return render(request, "importacion/importar.html", prompt)

	csv_file=request.FILES['archivo']

	if not csv_file.name.endswith('.csv'):
		messages.error(request,'el archivo no tiene el formato csv')

	datos=csv_file.read().decode('UTF-8')
	io_string=io.StringIO(datos)
	ban=0

	for fila in csv.reader(io_string, delimiter=';', quotechar="|"):
		try:
			pass
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass
		_, alu = Alumno.objects.update_or_create(
			nombre=fila[0],
			apellido=fila[1],
			dni=fila[2],
			mail=fila[3],
			telefono=fila[4],
			nacimiento=fila[5],
			titulo=fila[6],
			trabajo=fila[7],
			dispHoraria=fila[8],
			estudiosId=get_object_or_404(Estudio,id=fila[9])
		)
		a=Alumno.objects.latest('id')
		_, inscribir=Inscripcion.objects.update_or_create(
			cursoID=get_object_or_404(Curso,id=fila[10]),
			alumnoID=a
		)

	context={}
	return render(request,'importacion/importar.html',context)
