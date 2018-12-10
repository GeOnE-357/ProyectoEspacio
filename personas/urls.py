from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^(?P<tipo>\w+)/$', views.personasListar, name="personas-index"),# \w+ Este define que recibe un STRING.
url(r'^(?P<tipo>\w+)/Crear/$', views.personaNuevo, name='personas-crear'),
url(r'^(?P<tipo>\w+)/Usuario/Crear/$', views.personaUsuario, name='persona-usuario'),
url(r'^Detalle/(?P<tipo>\w+)/(?P<id>\d+)/$', views.personaDetalle, name="persona-detalle"),# \d+ Este define que recibe un INT.
url(r'^Editar/(?P<tipo>\w+)/(?P<id>\d+)/$', views.personaEditar, name="persona-editar"),
]