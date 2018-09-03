from django.db import models

class Alumno(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	dni = models.IntegerField(blank=True)
	edad = models.IntegerField(blank=True)
	trabajo = models.CharField(max_length=30)
	estudios = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre+" "+self.apellido


class Profesor(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	dni = models.IntegerField(blank=True)

	def __str__(self):
		return self.nombre+" "+self.apellido