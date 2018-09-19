from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.personasListar, name="personas-index"),
url(r'^Profesor/crear/$', views.profesorNuevo, name='profesor-crear'),
url(r'^Alumno/crear/$', views.alumnoNuevo, name='alumno-crear')
]