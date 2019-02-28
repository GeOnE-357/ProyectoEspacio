from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^Mostrar/MisCursos/(?P<usuario>\w+)/$', views.index, name="asistencia-index"),
url(r'^Mostrar/Inscriptos/(?P<curso>\d+)$', views.listarAlumnoCurso, name="alumno-index"),
url(r'^Mostrar/Inscriptos/Asistencia/(?P<curso>\d+)/(?P<id>\d+)/$', views.detalleAsistencia, name="alumno-asistencia"),
url(r'^Crear/Asistencia/(?P<curso>\d+)$', views.listarAsistenciaCurso, name="alumno-asistencia"),
url(r'^Realizar/Asistencia/$', views.AsistenciaCrear, name="asistencia-crear"),
]