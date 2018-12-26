from django.db import models

class Dependencia(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	telefono = models.BigIntegerField(blank=True)
	whatsapp = models.BigIntegerField(blank=True)

	def __str__(self):
		return self.nombre+" "+self.direccion

class Aula(models.Model):
	nombre = models.CharField(max_length=50)
	dependenciaId= models.ForeignKey('dependencia.Dependencia', blank=True, default="", on_delete=models.PROTECT)

	def __str__(self):
		return self.nombre

class DetalleAula(models.Model):
	"""docstring for ClassName"""
	aulaId=models.ForeignKey('dependencia.Aula', blank=True, default="", on_delete=models.PROTECT)
	diaId=models.ForeignKey('dependencia.Dia', blank=True, default="", on_delete=models.PROTECT)
	horaId=models.ForeignKey('dependencia.Horario', blank=True, default="", on_delete=models.PROTECT)
	estado=models.CharField(max_length=20)
	cursoID=models.ForeignKey('cursos.Curso',null=True, blank=True, default="", on_delete=models.PROTECT)
	def __str__(self):
		nombre=str(self.aulaId)+" - "+str(self.diaId)+" a las "+str(self.horaId)+" - "+str(self.cursoID)
		return nombre
		
	
class Dia(models.Model):
	dia = models.CharField(max_length=15) 
	def __str__(self):
		return self.dia

class Horario(models.Model):
	hora = models.IntegerField(blank=True)
	def __str__(self):
		hora=str(self.hora)
		return hora
