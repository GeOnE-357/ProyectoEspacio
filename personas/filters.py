from .models import Profesor, Alumno
import django_filters

class ProfesorFilter(django_filters.FilterSet):
    nombre=django_filters.CharFilter(label=False,)
    apellido=django_filters.CharFilter(label=False,)
    dni=django_filters.NumberFilter(label=False,)
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'dni']

class AlumnoFilter(django_filters.FilterSet):
    nombre=django_filters.CharFilter(label=False,)
    apellido=django_filters.CharFilter(label=False,)
    dni=django_filters.NumberFilter(label=False,)
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni']