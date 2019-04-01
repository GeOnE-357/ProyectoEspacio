from django.db import models

class Log(models.Model):
	dni = models.CharField(max_length=20)
	nombre = models.CharField(max_length=20)
	accion = models.CharField(max_length=20)
	tabla = models.CharField(max_length=20)
	objeto = models.IntegerField()
	fecha = models.DateTimeField(null=True)

	def __str__(self):
		return "El usuario: "+self.dni+" - "+self.nombre+" | Realizo la accion: "+self.accion+" | En la tabla: "+self.tabla+" en el objeto Id: "+str(self.objeto)+" | El dia "+str(self.fecha)

	class Meta:
		app_label = "control"
		db_table = "control_logs"