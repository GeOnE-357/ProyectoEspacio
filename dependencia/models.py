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

class DetalleAula(models.Model):
	"""docstring for ClassName"""
	aulaId=models.ForeignKey('dependencia.Aula', blank=True, default="", on_delete=models.PROTECT)
	diaId=models.ForeignKey('dependencia.Dia', blank=True, default="", on_delete=models.PROTECT)
		
	
class Dia(models.Model):
	dia = models.CharField(max_length=10) 

	def __str__(self):
		return self.dia

class Horario(models.Model):
	hora = models.IntegerField(blank=True)
		
class DetalleHorario(models.Model):
	"""docstring for DetalleAula"""
	aulaId=models.ForeignKey('dependencia.Dia',blank=True, default="",on_delete=models.PROTECT)
	horaId=models.ForeignKey('dependencia.Horario', blank=True, default="", on_delete=models.PROTECT)
	estado=models.CharField(max_length=10)
	def __str__(self):
		
		return self.estado