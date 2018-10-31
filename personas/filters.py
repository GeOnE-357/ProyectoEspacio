from .models import Profesor, Alumno
import django_filters

class ProfesorFilter(django_filters.FilterSet):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'dni']

class AlumnoFilter(django_filters.FilterSet):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni']