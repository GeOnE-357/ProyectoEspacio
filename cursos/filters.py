from .models import Curso, Materia
import django_filters

class CursoFilter(django_filters.FilterSet):
	class Meta:
		model = Curso
		fields = ['materiaID', 'profesorID', 'anio']

class MateriaFilter(django_filters.FilterSet):
	class Meta:
		model = Materia
		fields = ['nombre']