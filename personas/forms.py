from datetime import datetime, date, time, timedelta
from django.shortcuts import get_list_or_404, get_object_or_404
from django import forms
from .models import Profesor, Alumno
from espacio.validators import validate_dni, validate_cel, validate_tel, validate_str, validate_str

class profesorForm(forms.ModelForm):
	LISTA=[]
	anio=date.today().year
	inicio=1900
	while inicio <= anio :
		LISTA.append(inicio)
		inicio+=1
	LISTA.reverse()
	ESTUDIOS_CHOICES=(('Primario Cursando','Primario Cursando'),('Primario Completo','Primario Completo'),('Primario Incompleto','Primario Incompleto'),('Secundario Cursando','Secundario Cursando'),('Secundario Completo','Secundario Completo'),('Secundario Incompleto','Secundario Incompleto'),('Terciario Cursando','Terciario Cursando'),('Terciario Completo','Terciario Completo'),('Terciario Incompleto','Terciario Incompleto'),('Universitario Cursando','Universitario Cursando'),('Universitario Completo','Universitario Completo'),('Universitario Incompleto','Universitario Incompleto'),)
	nombre=forms.CharField(validators=[validate_str])
	apellido=forms.CharField(validators=[validate_str])
	dni=forms.CharField(validators=[validate_dni])
	telefono=forms.CharField(validators=[validate_cel])
	nacimiento=forms.DateField(widget = forms.SelectDateWidget(years=LISTA))
	estudios=forms.ChoiceField(choices=ESTUDIOS_CHOICES, label="Estudios:", widget=forms.Select(), required=True)
	class Meta:
		model = Profesor
		fields = ('nombre', 'apellido', 'dni', 'mail', 'telefono', 'nacimiento', 'titulo', 'estudios', 'expediente')

class alumnoForm(forms.ModelForm):
	LISTA=[]
	anio=date.today().year
	inicio=1900
	while inicio <= anio :
		LISTA.append(inicio)
		inicio+=1
	LISTA.reverse()
	
	ESTUDIOS_CHOICES=(('Primario Cursando','Primario Cursando'),('Primario Completo','Primario Completo'),('Primario Incompleto','Primario Incompleto'),('Secundario Cursando','Secundario Cursando'),('Secundario Completo','Secundario Completo'),('Secundario Incompleto','Secundario Incompleto'),('Terciario Cursando','Terciario Cursando'),('Terciario Completo','Terciario Completo'),('Terciario Incompleto','Terciario Incompleto'),('Universitario Cursando','Universitario Cursando'),('Universitario Completo','Universitario Completo'),('Universitario Incompleto','Universitario Incompleto'),)
	TRABAJO_CHOICES=(('No estoy trabajando','No estoy trabajando'),('Trabajo de manera informal','Trabajo de manera informal'),('Estoy en relación de dependencia','Estoy en relación de dependencia'),('Soy independiente','Soy independiente'))
	#HORARIOS=(("Mañana", "Mañana"),("Tarde", "Tarde"),("Noche","Noche"))
	nombre=forms.CharField(validators=[validate_str])
	apellido=forms.CharField(validators=[validate_str])
	dni=forms.CharField(validators=[validate_dni])
	telefono=forms.CharField(validators=[validate_cel])
	nacimiento=forms.DateField(widget=forms.SelectDateWidget(years=LISTA))
	#dispHoraria=forms.ChoiceField(choices =HORARIOS , label="Disponibilidad:", widget=forms.Select(), required=True)
	estudios=forms.ChoiceField(choices=ESTUDIOS_CHOICES, label="Estudios:", widget=forms.Select(), required=True)
	trabajo=forms.ChoiceField(choices=TRABAJO_CHOICES, label="Trabajo:", widget=forms.Select(), required=True)
	class Meta:
		model = Alumno
		fields = ('nombre', 'apellido', 'dni', 'mail', 'telefono', 'nacimiento', 'estudios', 'trabajo')