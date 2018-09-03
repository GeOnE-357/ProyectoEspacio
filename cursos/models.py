from django.db import models

class Curso(models.Model):
	profesor=models.ForeignKey("personas.Profesor", blank=True, default="",on_delete=models.PROTECT)
	nombre=models.CharField(max_length=30)
	horario=models.IntegerField(blank=True)
	cantidad=models.IntegerField(blank=True)

	def __str__(self):
		return self.nombre


class Clase(models.Model):
	aula=models.ForeignKey("cursos.Aula", blank=True, default="",on_delete=models.PROTECT)
	computadoras=models.ForeignKey("computadoras.Computadora", blank=True, default="",on_delete=models.PROTECT)

	def __unicode__(self):
		return str(self.aula)


class Aula(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre