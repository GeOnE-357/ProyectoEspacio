from django import forms
from .models import Dependencia, Aula,DetalleAula, Dia, Horario

class dependenciaForm(forms.ModelForm):
	model = Dependencia
    fields = ('nombre', 'direccion', 'telefono', 'whatsapp')


class aulaForm(forms.ModelForm):

	model = Aula
    fields = ('nombre', 'dependenciaId')

class detalleAulaForm(forms.ModelForm):
	model=DetalleAula
	fields=('aulaId','diaId','horaId','horaId','cursoID')            