from django import forms

class ImportarForm(forms.Form):
	archivo=forms.FileField()