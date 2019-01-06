from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.importar, name='importacion-index'),
]