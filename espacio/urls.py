"""espacio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url #importe las librerias include y url.
from django.contrib import admin
from . import views #llamo a los views, para poder tener la pagina de inicio.

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$', views.home, name="home"),
    url(r'^Personas/', include('personas.urls')), #Incluido el archivo urls.py de la app personas.
    url(r'^dependencia/', include('dependencia.urls')),
    url(r'^Usuario/Registrar/$', views.registrarUsuario, name="usuario-crear"),
    url(r'^Usuario/Login/$', views.loginUsuario, name="login"),
    url(r'^Usuario/Logout/$', views.logoutUsuario, name="logout"),
]
