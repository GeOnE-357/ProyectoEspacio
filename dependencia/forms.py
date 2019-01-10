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
	
	ESTADO_CHOICES = (
    ("disponible", "Disponible"),
    ("en curso", "En curso"),)

	estado = forms.ChoiceField(choices = ESTADO_CHOICES, label="Estado:", widget=forms.Select(), required=True)
	class Meta:
		model=DetalleAula 
		fields=('estado','cursoID')            