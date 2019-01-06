from django.shortcuts import render
from django.contrib import messages
import csv,io
from personas.models import Alumno,Estudio
from cursos.models import Inscripcion

def importar(request):
	prompt={
		'datos':"El orden debe ser nombre,apellido,dni,mail,telefono,nacimiento,titulo,trabajo,disponibilidad, estudios, curso"
	}
	if request.method== "GET":
		return render(request,"importacion/importar.html",prompt)

	csv_file=request.FILES['archivo']

	if not csv_file.name.endswith('.csv'):
		messages.error(request,'el archivo no tiene el formato csv')

	datos=csv_file.read().decode('UTF-8')
	io_string=io.StringIO(datos)
	alu=Alumno.objects.all()
	ban=0

	for fila in csv.reader(io_string, delimiter=';', quotechar="|"):
		for a in alu:
			if fila[2] == a.dni:
				ban=1

		if ban==0:
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
			alu.estudiosId=fila[9]
			alu.save()
			a=Alumno.objects.latest('id')
			inscribir=Inscripcion()
			inscribir.cursoID=fila[10]
			inscribir.alumnoID=a
			inscribir.save()
		else:
			inscribir=Inscripcion()
			inscribir.cursoID=fila[10]
			inscribir.alumnoID=fila[0]
			inscribir.save()
	context={'RESULTADO':'NO SE XD'}
	return render(request,'importacion/importar.html',context)
