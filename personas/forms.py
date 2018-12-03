from django import forms
from .models import Profesor, Alumno, Estudio

class profesorForm(forms.ModelForm):
	nacimiento=forms.DateField(widget = forms.SelectDateWidget())
	class Meta:
		model = Profesor
		fields = ('nombre', 'apellido', 'dni', 'mail', 'telefono', 'nacimiento', 'titulo', 'estudiosId', 'expediente')


class alumnoForm(forms.ModelForm):
	nacimiento=forms.DateField(widget = forms.SelectDateWidget())
	class Meta:
		model = Alumno
		fields = ('nombre', 'apellido', 'dni', 'mail', 'telefono', 'nacimiento', 'titulo', 'estudiosId', 'trabajo', 'dispHoraria')