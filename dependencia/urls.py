from django.conf.urls import url
from . import views 

urlpatterns = [
url(r'^$', views.indexDependencia, name="index_dependencia"),
url(r'^mostrar/', views.dependencias, name="dependencias"),


]