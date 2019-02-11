from django.conf.urls import url
from . import views 

urlpatterns = [
url(r'^$', views.dependencias, name="dependencia"),
url(r'^Mostrar/Aulas/(?P<id>\d+)$', views.aulas, name="aulas"),
url(r'^Mostrar/DetalleAula/(?P<id>\d+)$',views.detalleAula, name="detalleAula"),
url(r'^Mostrar/DetalleAula/Editar/(?P<id>\d+)$',views.detalleEditar, name="detalleEditar"),
url(r'^Mostrar/DetalleAula/Cargar/(?P<id>\d+)/(?P<tipo>\w+)$',views.cargarCurso, name="cargarCurso"),
url(r'^Crear/Detalle/(?P<aula>\d+)$', views.detalleCrear, name='detallecrear'),
url(r'^Crear/$', views.dependenciaCrear, name='dependenciacrear'),
url(r'^Crear/Aula/(?P<id>\d+)/$', views.crearAula, name='aulacrear')

]