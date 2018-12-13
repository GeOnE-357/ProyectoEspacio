
#asistencia de un curso

asis=Alumno.objects.raw('SELECT alumno.*,curso.*,inscripcion.* FROM alumno,curso,incripcion WHERE alumno.ID=incripcion.alumnoID_ID AND curso.id=incripcion.cursoID_id AND curso.profesorID_id=variable de la sesion')


def listarAlumnoCurso(request, curso):
	inscripto=Inscripcion.objects.all(cursoID=curso)
	for a in inscripto.alumnoid:
		alumno=Alumno.objects.get(id=a)
		lista.append(alumno)
	return render (request, 'asistencia/detalle.html', {'lista':lista})