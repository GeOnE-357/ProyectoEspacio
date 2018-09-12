from django.contrib import admin
from .models import Persona, Profesor, Alumno

admin.site.register(Profesor)
admin.site.register(Alumno)
