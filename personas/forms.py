from datetime import datetime, date, time, timedelta
from django.shortcuts import get_list_or_404, get_object_or_404
from django import forms
from .models import Profesor, Alumno, Estudio

class profesorForm(forms.ModelForm):
	LISTA=[]
	anio=date.today().year
	inicio=1900
	while inicio <= anio :
		LISTA.append(inicio)
		inicio+=1
	LISTA.reverse()

	nacimiento=forms.DateField(widget = forms.SelectDateWidget(years=LISTA))
	estudiosId=forms.ModelChoiceField(queryset=Estudio.objects.all(), label="Estudios:", required=True)
	class Meta:
		model = Profesor
		fields = ('nombre', 'apellido', 'dni', 'mail', 'telefono', 'nacimiento', 'titulo', 'estudiosId', 'expediente')


class alumnoForm(forms.ModelForm):
	LISTA=[]
	anio=date.today().year
	inicio=1900
	while inicio <= anio :
		LISTA.append(inicio)
		inicio+=1
	LISTA.reverse()
	
	HORARIOS=(("Mañana", "Mañana"),("Tarde", "Tarde"),("Noche","Noche"))

	nacimiento=forms.DateField(widget=forms.SelectDateWidget(years=LISTA))
	dispHoraria=forms.ChoiceField(choices =HORARIOS , label="Disponibilidad:", widget=forms.Select(), required=True)
	estudiosId=forms.ModelChoiceField(queryset=Estudio.objects.all(), label="Estudios:", required=True)
	class Meta:
		model = Alumno
		fields = ('nombre', 'apellido', 'dni', 'mail', 'telefono', 'nacimiento', 'titulo', 'estudiosId', 'trabajo', 'dispHoraria')