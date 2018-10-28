from django import forms
from .models import Curso, Materia, Mes
from personas.models import Profesor

class CursoForm(forms.ModelForm):
	anio = forms.IntegerField(required=True, label='Año:')
	class Meta:
		model = Curso
		fields = ('materiaID', 'modulo', 'profesorID', 'mes', 'anio', 'estado')