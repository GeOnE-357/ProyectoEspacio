from django.db import models
# Create your models here.
class Curso(models.Model):
	"""docstring for Curso"""
	materiaID=models.ForeignKey('cursos.Materia',blank=True,default="",on_delete=models.PROTECT)
	modulo=models.CharField(max_length=15)
	profesorID=models.ForeignKey('personas.Profesor', blank=True, default="", on_delete=models.PROTECT)
	fInicio=models.DateField(auto_now=False, auto_now_add=False)
	fFin=models.DateField(auto_now=False, auto_now_add=False)
	estado=models.CharField(max_length=15)
	cantClases=models.IntegerField(blank=True)
	def __str__(self):
		nombre=str(self.materiaID)+" "+str(self.modulo)+" - "+str(self.profesorID)
		return nombre

	def nombre_tabla(self):
		tabla=str(self._meta.db_table)
		return tabla


class Materia(models.Model):
	nombre=models.CharField(max_length=50)
	tipo=models.CharField(max_length=20)
	def __str__(self):
		return self.nombre

class Inscripcion(models.Model):
	cursoID=models.ForeignKey('cursos.Curso',blank=True,default="",on_delete=models.CASCADE)
	alumnoID=models.ForeignKey('personas.Alumno',blank=True,default="",on_delete=models.CASCADE)
	fecha=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		nombre=str(self.alumnoID)+" - "+str(self.cursoID)
		return nombre