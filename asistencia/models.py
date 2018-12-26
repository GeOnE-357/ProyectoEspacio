from django.db import models

class Asistencia(models.Model):
	presente=models.BooleanField(default=False)
	inscripcionID=models.ForeignKey('cursos.Inscripcion',blank=True, default="", on_delete=models.PROTECT)
	fecha=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		nombre=str(self.inscripcionID)
		return nombre
