from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^Mostrar/MisCursos/(?P<usuario>\w+)/$', views.index, name="Asistencia-index"),
url(r'^$', views.listarCurso, name="listarCurso"),
]