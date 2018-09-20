from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.personasListar, name="personas-index"),
url(r'^Profesor/crear/$', views.profesorNuevo, name='profesor-crear'),
url(r'^Alumno/crear/$', views.alumnoNuevo, name='alumno-crear'),
url(r'^Profe-Detalle/(?P<id>\d+)/$', views.profesorDetalle, name="profesor-detalle"),
url(r'^Alum-Detalle/(?P<id>\d+)/$', views.alumnoDetalle, name="alumno-detalle"),
]