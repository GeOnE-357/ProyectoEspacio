from django import forms
from .models import Dependencia, Aula,DetalleAula, Dia, Horario
from cursos.models import Curso

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
	dia1=forms.ModelChoiceField(queryset=Dia.objects.all(), required=True)
	dia2=forms.ModelChoiceField(queryset=Dia.objects.all(), required=False)
	hora1=forms.ModelChoiceField(queryset=Horario.objects.all(), required=True)
	hora2=forms.ModelChoiceField(queryset=Horario.objects.all(), required=True)