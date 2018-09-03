from django.db import models

class Computadora(models.Model):
	nombre =models.CharField(max_length=30)
	cantidad=models.IntegerField(blank=True)

	def __str__(self):
		return self.nombre