from django import forms
from .models import Dependencia, Aula,DetalleAula, Dia, Horario
from cursos.models import Curso
from django.forms.widgets import CheckboxSelectMultiple
from espacio.validators import validate_dni, validate_cel, validate_tel, validate_str, validate_dir

class DependenciaForm(forms.ModelForm):
	telefono=forms.IntegerField(validators=[validate_tel])
	direccion=forms.CharField(validators=[validate_dir])
	class Meta:
		model = Dependencia 
		fields= ('nombre', 'direccion', 'telefono', 'whatsapp')

class MesForm(forms.Form):
	MES_CHOICES = (
	("enero", "Enero"),
	("febrero", "Febrero"),
	("marzo", "Marzo"),
	("abril", "Abril"),
	("mayo", "Mayo"),
	("junio", "Junio"),
	("julio", "Julio"),
	("agosto", "Agosto"),
	("septiembre", "Septiembre"),
	("octubre", "Octubre"),
	("noviembre", "Noviembre"),
	("diciembre", "Diciembre"),)
	mes = forms.ChoiceField(choices = MES_CHOICES, label="Mes:", widget=forms.Select(), required=True)
	anio=forms.DateField(label="Año:")

class AulaForm(forms.ModelForm):
	class Meta:
		model = Aula 
		fields = ('nombre',)


class DetalleAulaForm(forms.ModelForm):
	
	ESTADO_CHOICES = (
	("disponible", "Disponible"),
	("en curso", "En curso"),)

	estado = forms.ChoiceField(choices = ESTADO_CHOICES, label="Estado:", widget=forms.Select(), required=True)
	cursoID= forms.ModelChoiceField(queryset=Curso.objects.all(), label="Curso:",required=True)
	class Meta:
		model=DetalleAula 
		fields=('estado','cursoID')            


class CargarCursoForm(forms.Form):
	curso=forms.ModelChoiceField(queryset=Curso.objects.all(), required=True)
	dia=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Dia.objects.all())
	hora1=forms.ModelChoiceField(queryset=Horario.objects.all(), label="De:",required=True)
	hora2=forms.ModelChoiceField(queryset=Horario.objects.all(), label="A:",required=True)