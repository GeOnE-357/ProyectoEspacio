from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^(?P<tipo>\w+)/$', views.personasListar, name="personas-index"),# \w+ Este define que recibe un STRING.
url(r'^Profesor/crear/$', views.profesorNuevo, name='profesor-crear'),
url(r'^Alumno/crear/$', views.alumnoNuevo, name='alumno-crear'),
url(r'^Detalle/Alumno/(?P<id>\d+)/$', views.alumDetalle, name="alumno-detalle"),# \d+ Este define que recibe un INT.
url(r'^Detalle/Profesor/(?P<id>\d+)/$', views.profDetalle, name="profesor-detalle"),
]