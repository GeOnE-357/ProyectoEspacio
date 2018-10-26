from django import forms
from .models import Curso, Materia,
from personas.models import Profesor

class cursoForm(forms.ModelForm):
	class meta:
		model = Curso
		fields = ('materiaId', 'modulo', 'profesorID', 'mes', 'anio', 'estado')