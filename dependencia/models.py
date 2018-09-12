from django.db import models

class Dependencia(models.Model):
	nombre = models.CharField(max_length=10)
	direccion = models.CharField(max_length=15)
	telefono = models.IntegerField(blank=True)
	whatsapp = models.IntegerField(blank=True)

	def __str__(self):
		return self.nombre+" "+self.direccion

class Aula(models.Model):
	nombre = models.CharField(max_length=10)
	dependenciaId= models.ForeignKey('dependencia.Dependencia', blank=True, default="", on_delete=models.PROTECT)

	def __str__(self):
		return self.nombre

class Dia(models.Model):
	dia = models.CharField(max_length=10)
	aulaId = models.ForeignKey('dependencia.Aula', blank=True, default="", on_delete=models.PROTECT)

	def __str__(self):
		return self.dia

class Horario(models.Model):
	hora = models.IntegerField(blank=True)
	estado = models.CharField(max_length=10)
	diaId=models.ForeignKey('dependencia.Dia', blank=True, default="", on_delete=models.PROTECT)
	
	def __str__(self):
		return self.estado