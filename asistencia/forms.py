from django import forms
from cursos.models import Inscripcion
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
	class Meta:
		model = Asistencia
		fields = ('presente', 'inscripcionID')