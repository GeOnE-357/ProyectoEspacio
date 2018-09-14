from django.db import models

# Create your models here.
class Curso(models.Model):
	"""docstring for Curso"""
	materia=models.CharField(max_length=30)
	modulo=models.IntegerField(blank=True)
	fechaI=models.DateField(null=False, max_length=50)
	fechaF=models.DateField(null=False, max_length=50)
	profesorID=models.ForeignKey('personas.Profesor', blank=True, default="", on_delete=models.PROTECT)
	
	def __str__(self):
		return self.materia
