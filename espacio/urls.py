from django.conf.urls import include, url #importe las librerias include y url.
from django.contrib import admin
from . import views #llamo a los views, para poder tener la pagina de inicio.

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', views.home, name="home"),
    url(r'^Persona/', include('personas.urls')), #Incluido el archivo urls.py de la app personas.
    url(r'^Dependencia/', include('dependencia.urls')),
    url(r'^Control/', include('control.urls')),
    url(r'^(?P<tipo>\w+)/Registrar/$', views.registrarUsuario, name="usuario-crear"),
    url(r'^Usuario/Login/$', views.loginUsuario, name="login"),
    url(r'^Usuario/Logout/$', views.logoutUsuario, name="logout"),
    url(r'^Usuario/Password/$', views.passwordUsuario, name="password"),
    url(r'^Curso/', include('cursos.urls')),
    url(r'^Asistencia/', include('asistencia.urls')),
    url(r'^Importacion/',include('importacion.urls'))
]
