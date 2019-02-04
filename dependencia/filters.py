from .models import Dependencia, Aula
import django_filters

class DependenciaFilter(django_filters.FilterSet):
	class Meta:
		model = Dependencia
		fields = ['nombre']

class AulaFilter(django_filters.FilterSet):
	class Meta:
		model = Dependencia
		fields = ['nombre']