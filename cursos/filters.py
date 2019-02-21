from .models import Curso, Materia
from personas.models import Profesor
import django_filters

class CursoFilter(django_filters.FilterSet):
	materiaID=django_filters.ModelChoiceFilter(queryset=Materia.objects.all(), label=False,)
	profesorID=django_filters.ModelChoiceFilter(queryset=Profesor.objects.all(), label=False,)
	fInicio=django_filters.NumberFilter(field_name='fInicio', lookup_expr='year', label=False)
	class Meta:
		model = Curso
		fields = ['materiaID', 'profesorID', 'fInicio']

class MateriaFilter(django_filters.FilterSet):
	nombre=django_filters.CharFilter(label=False, )
	class Meta:
		model = Materia
		fields = ['nombre']