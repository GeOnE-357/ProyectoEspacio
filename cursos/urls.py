from django.conf.urls import url
from . import views 

urlpatterns = [
url(r'^$', views.cursosListar, name="cursos-index"),
url(r'^Materia/$', views.materiasListar, name="materias-index"),
]