from django.conf.urls import url
from . import views 

urlpatterns = [
url(r'^$', views.dependencias, name="dependencia"),
url(r'^Mostrar/Aulas/(?P<id>\d+)$', views.aulasLista, name="aulaLista"),
url(r'^Crear/Aula/Mes/(?P<id>\d+)$',views.aula, name="aula"),
url(r'^Buscar/Aula/(?P<id>\d+)$',views.aulaBuscar, name="aulaBuscar"),
url(r'^Mostrar/Aula/(?P<id>\d+)/(?P<mes>\w+)/(?P<anio>\w+)/$',views.aulaMes, name="aulaMes"),
url(r'^Mostrar/Aula/DetalleEditar/(?P<id>\d+)$',views.detalleEditar, name="detalleEditar"),
url(r'^Mostrar/Aula/Cargar/(?P<id>\d+)/(?P<tipo>\w+)$',views.cargarCurso, name="cargarCurso"),
url(r'^Crear/Aula/Horarios/(?P<aula>\d+)/(?P<mes>\w+)/(?P<anio>\d+)/$', views.horarioCrear, name='horarioCrear'),
url(r'^Crear/$', views.dependenciaCrear, name='dependenciaCrear'),
url(r'^Crear/Aula/(?P<id>\d+)/$', views.crearAula, name='crearAula')
]