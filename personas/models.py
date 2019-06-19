from django.db import models
from django.contrib.auth.models import AbstractUser, User

class Persona(models.Model):
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	dni=models.BigIntegerField(blank=True)
	mail=models.EmailField(max_length=30)
	telefono=models.BigIntegerField(blank=True)
	nacimiento=models.DateField(auto_now=False, auto_now_add=False)
	estudios=models.CharField(max_length=30)
	class Meta:
		abstract = True

class Profesor(Persona):
	titulo=models.CharField(max_length=80)
	expediente=models.IntegerField(blank=True)
	user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return "Prof. "+self.nombre +" "+ self.apellido

class Alumno(Persona):	
	trabajo=models.CharField(max_length=50)
	def __str__(self):
		return self.nombre +" "+ self.apellido