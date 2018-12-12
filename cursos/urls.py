from django.conf.urls import url
from . import views 

urlpatterns = [
url(r'^$', views.cursosListar, name="cursos-index"),
url(r'^Crear/$', views.cursosCrear, name="cursos-crear"),
url(r'^(?P<id>\d+)/Editar/$', views.cursosEditar, name="cursos-editar"),
url(r'^Materia/$', views.materiasListar, name="materias-index"),
url(r'^Materia/Crear/$', views.materiasCrear, name="materias-crear"),
url(r'^Materia/(?P<id>\d+)/Editar/$', views.materiasEditar, name="materias-editar"),
url(r'^Inscribir/(?P<tipo>\w+)/(?P<id>\d+)/$', views.inscripcionCrear, name="inscribir-crear"),
]