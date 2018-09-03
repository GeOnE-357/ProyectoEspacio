from django.contrib import admin
from .models import Curso, Clase, Aula

admin.site.register(Aula)
admin.site.register(Clase)
admin.site.register(Curso)