from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^(?P<tipo>\w+)/$', views.personasListar, name="personas-index"),# \w+ Este define que recibe un STRING.
url(r'^(?P<tipo>\w+)/crear/$', views.personaNuevo, name='personas-crear'),
url(r'^Detalle/(?P<tipo>\w+)/(?P<id>\d+)/$', views.personaDetalle, name="persona-detalle"),# \d+ Este define que recibe un INT.
]