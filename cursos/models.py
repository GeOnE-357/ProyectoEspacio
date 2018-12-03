from django.db import models

# Create your models here.
class Curso(models.Model):
	"""docstring for Curso"""
	materiaID=models.ForeignKey('cursos.Materia',blank=True,default="",on_delete=models.PROTECT)
	modulo=models.IntegerField(blank=True)
	profesorID=models.ForeignKey('personas.Profesor', blank=True, default="", on_delete=models.PROTECT)
	fInicio=models.DateField(auto_now=False, auto_now_add=False)
	fFin=models.DateField(auto_now=False, auto_now_add=False)
	anio=models.IntegerField(blank=True)
	estado=models.CharField(max_length=15)
	cantClases=models.IntegerField(blank=True)
	def __unicode__(self):
		return self.materiaID

class Materia(models.Model):
	nombre=models.CharField(max_length=50)
	tipo=models.CharField(max_length=20)
	def __str__(self):
		return self.nombre

class Inscripcion(models.Model):
	cursoID=models.ForeignKey('cursos.Curso',blank=True,default="",on_delete=models.PROTECT)
	alumnoID=models.ForeignKey('personas.Alumno',blank=True,default="",on_delete=models.PROTECT)
	fecha=models.DateTimeField(auto_now_add=True)