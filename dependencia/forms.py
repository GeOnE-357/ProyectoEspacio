from django import forms
from .models import Dependencia, Aula,DetalleAula, Dia, Horario

class DependenciaForm(forms.ModelForm):
	class Meta:
		model = Dependencia 
		fields= ('nombre', 'direccion', 'telefono', 'whatsapp')


class AulaForm(forms.ModelForm):
	class Meta:
		model = Aula 
		fields = ('nombre', 'dependenciaId')

class DetalleAulaForm(forms.ModelForm):
	class Meta:
		model=DetalleAula 
		fields=('aulaId','diaId','horaId','horaId','cursoID')            