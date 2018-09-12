from django.db import models

class Persona(models.Model):
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	dni=models.IntegerField(blank=True)
	email=models.EmailField(max_length=30)
	telefono=models.IntegerField(blank=True)
	nacimiento=models.DateField(auto_now=False, auto_now_add=False)

	class Meta:
		abstract = True


class Profesor(Persona):
	legajo=models.IntegerField(blank=True)

class Alumno(Persona):	
	trabajo=BooleanField(default=True) 
