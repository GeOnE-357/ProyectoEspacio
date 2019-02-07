from django import forms
from .models import Curso, Materia,Inscripcion
from personas.models import Profesor, Alumno

class CursoForm(forms.ModelForm):
	anio = forms.IntegerField(required=True, label='Año:')
	fInicio=forms.DateField(widget = forms.SelectDateWidget(), label='Fecha de Inicio:')
	fFin=forms.DateField(widget = forms.SelectDateWidget(), label='Fecha de Finalizacion:')
	cantClases=forms.IntegerField(required=True, label='Cantidad de Clases:')
	materiaID=forms.ModelChoiceField(queryset=Materia.objects.all(), label="Materia:", required=True)
	profesorID=forms.ModelChoiceField(queryset=Profesor.objects.all(), label="Profesor:", required=True)
	class Meta:
		model = Curso
		fields = ('materiaID', 'modulo', 'profesorID', 'cantClases', 'fInicio', 'fFin', 'anio', 'estado')

class MateriaForm(forms.ModelForm):
	
	TIPO_CHOICES = (
    ("Tecnológico", "Tecnológico"),
    ("Oficio Tradicional", "Oficio Tradicional"),)

	tipo = forms.ChoiceField(choices = TIPO_CHOICES, label="Tipo:", widget=forms.Select(), required=True)
	nombre = forms.CharField(required=True)
	class Meta:
		model = Materia
		fields = ('nombre', 'tipo')

class InscripcionForm(forms.ModelForm):
	class Meta:
		model = Inscripcion
		fields = ('cursoID',)