from django.db import models

class Presente(models.Model):
	curso=models.ForeignKey('cursos.Curso', blank=True, default="",on_delete=models.PROTECT)
	alumno=models.ForeignKey('personas.Alumno', blank=True, default="",on_delete=models.PROTECT)
	clase=models.ForeignKey('cursos.Clase', blank=True, default="",on_delete=models.PROTECT)
	estado=models.IntegerField(blank=True)