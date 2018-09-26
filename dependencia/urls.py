from django.conf.urls import url
from . import views 

urlpatterns = [
url(r'^$', views.dependencias, name="dependencia"),
url(r'^aulas/(?P<id>\d+)$', views.aulas, name="aulas"),
url(r'^detalleAula/(?P<id>\d+)$',views.detalleAula, name="detalleAula"),

]