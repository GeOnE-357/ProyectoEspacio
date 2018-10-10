from django.conf.urls import url
from . import views 

urlpatterns = [
url(r'^$', views.dependencias, name="dependencia"),
url(r'^Mostrar/Aulas/(?P<id>\d+)$', views.aulas, name="aulas"),
url(r'^Mostrar/DetalleAula/(?P<id>\d+)$',views.detalleAula, name="detalleAula"),
url(r'^Crear/Detalle/$', views.detalleCrear, name='detallecrear'),
url(r'^Crear/$', views.dependenciaCrear, name='dependenciacrear'),

]