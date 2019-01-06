from django import forms

class ImportacionForm(forms.ModelForm):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
