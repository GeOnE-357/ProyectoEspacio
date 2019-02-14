from django import forms
from .models import Dependencia, Aula,DetalleAula, Dia, Horario
from cursos.models import Curso
from django.forms.widgets import CheckboxSelectMultiple

class DependenciaForm(forms.ModelForm):
	class Meta:
		model = Dependencia 
		fields= ('nombre', 'direccion', 'telefono', 'whatsapp')


class AulaForm(forms.ModelForm):
	class Meta:
		model = Aula 
		fields = ('nombre',)


class DetalleAulaForm(forms.ModelForm):
	
	ESTADO_CHOICES = (
    ("disponible", "Disponible"),
    ("en curso", "En curso"),)

	estado = forms.ChoiceField(choices = ESTADO_CHOICES, label="Estado:", widget=forms.Select(), required=True)
	class Meta:
		model=DetalleAula 
		fields=('estado','cursoID')            


class CargarCursoForm(forms.Form):
	curso=forms.ModelChoiceField(queryset=Curso.objects.all(), required=True)
	dia=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Dia.objects.all())
	hora1=forms.ModelChoiceField(queryset=Horario.objects.all(), label="De:",required=True)
	hora2=forms.ModelChoiceField(queryset=Horario.objects.all(), label="A:",required=True)