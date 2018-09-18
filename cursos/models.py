from django.db import models

# Create your models here.
class Curso(models.Model):
	"""docstring for Curso"""
	materiaID=models.ForeignKey('cursos.Materia',blank=True,default="",on_delete=models.PROTECT)
	modulo=models.IntegerField(blank=True)
	profesorID=models.ForeignKey('personas.Profesor', blank=True, default="", on_delete=models.PROTECT)
	mes=models.CharField(max_length=10)
	anio=models.IntegerField(blank=True)
	estado=models.CharField(max_length=15)
	def __str__(self):
		return self.mes + self.estado

class Materia(models.Model):
	nombre=models.CharField(max_length=50)
	tipo=models.CharField(max_length=20)
	def __str__(self):
		return self.mes + self.estado



class Asistencia(models.Model):
	"""docstring for Asistencia"""
	cursoID=models.ForeignKey('cursos.Curso',blank=True,default="",on_delete=models.PROTECT)
	alumnoID=models.ForeignKey('personas.Alumno',blank=True,default="",on_delete=models.PROTECT)
	fecha=models.DateTimeField(auto_now_add=True)
	
		

