from .models import Dependencia, Aula
import django_filters

class DependenciaFilter(django_filters.FilterSet):
	nombre=django_filters.CharFilter(label=False, )
	class Meta:
		model = Dependencia
		fields = ['nombre']

class AulaFilter(django_filters.FilterSet):
	nombre=django_filters.CharFilter(label=False, )
	class Meta:
		model = Dependencia
		fields = ['nombre']