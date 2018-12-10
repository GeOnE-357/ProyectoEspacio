from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^Mostrar/MisCursos/(?P<usuario>\w+)/$', views.index, name="asistencia-index"),
url(r'^Mostrar/MisCursos/Inscriptos/(?P<curso>\d+)$', views.listarAlumnoCurso, name="alumno-index"),
]