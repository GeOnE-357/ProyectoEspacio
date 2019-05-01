from django.conf.urls import url
from . import views 

urlpatterns = [
url(r'^$', views.dependencias, name="dependencia"),
url(r'^Mostrar/Aulas/(?P<id>\d+)$', views.aulaLista, name="aulaLista"),
url(r'^Mostrar/Aula/(?P<id>\d+)$',views.aulaMes, name="aula"),
url(r'^Mostrar/Aula/(?P<id>\d+)/(?P<mes>\w+)/(?P<anio>\w+)/$',views.aulaDetalle, name="aulaMes"),
url(r'^Mostrar/Aula/DetalleEditar/(?P<id>\d+)$',views.detalleEditar, name="detalleEditar"),
url(r'^Mostrar/Aula/Cargar/(?P<id>\d+)/(?P<tipo>\w+)$',views.cargarCurso, name="cargarCurso"),
url(r'^Crear/Aula/Horarios/(?P<aula>\d+)/(?P<mes>\w+)/(?P<anio>\d+)/$', views.horarioCrear, name='horarioCrear'),
url(r'^Crear/$', views.dependenciaCrear, name='dependenciaCrear'),
url(r'^Crear/Aula/(?P<id>\d+)/$', views.crearAula, name='crearAula')
]