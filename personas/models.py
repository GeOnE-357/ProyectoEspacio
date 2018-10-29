from django.db import models
from django.contrib.auth.models import AbstractUser

class Persona(models.Model):
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	dni=models.IntegerField(blank=True)
	mail=models.EmailField(max_length=30)
	telefono=models.IntegerField(blank=True)
	nacimiento=models.DateField(auto_now=False, auto_now_add=False)
	titulo=models.CharField(max_length=30)
	estudiosId=models.ForeignKey('personas.Estudio', blank=True, default="", on_delete=models.PROTECT)

	class Meta:
		abstract = True

class Profesor(Persona):
	expediente=models.IntegerField(blank=True)
	def __str__(self):
		return self.nombre +" "+ self.apellido

class Alumno(Persona):	
	trabajo=models.BooleanField(default=True)
	dispHoraria=models.CharField(max_length=30)
	def __str__(self):
		return self.nombre +" "+ self.apellido

class Estudio(models.Model):
	nivel=models.CharField(max_length=30)
	estado=models.CharField(max_length=30)

	def __str__(self):
		return self.nivel+" / "+self.estado