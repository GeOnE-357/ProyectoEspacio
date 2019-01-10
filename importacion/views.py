from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
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
	

	for fila in csv.reader(io_string, delimiter=';', quotechar="|"):
		alu=Alumno.objects.all()
		ban=0
		for a in alu:
			if str(fila[2]) == str(a.dni):
				ban=1

		if ban == 0:
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
			al=Alumno.objects.latest('id')
			inscribir=Inscripcion()
			inscribir.cursoID=get_object_or_404(Curso,id=fila[10])
			inscribir.alumnoID=al
			inscribir.save()
		else:
			inscribir=Inscripcion()
			inscribir.cursoID=get_object_or_404(Curso,id=fila[10])
			inscribir.alumnoID=get_object_or_404(Alumno,dni=fila[2])
			inscribir.save()
	context={"resul":"Todo Salio ok XD"}
	return render(request,'importacion/importar.html',context)
